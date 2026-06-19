import email
import re
import quopri
from email.header import decode_header
from typing import Optional, Dict, List


def parse_raw_email(raw_email: str) -> Dict:
    """
    Raw email text ko parse karke useful parts nikalта hai
    """
    try:
        msg = email.message_from_string(raw_email)
    except Exception:
        return {"error": "Email parse nahi hua"}

    subject = _decode_subject(msg.get("Subject", "No Subject"))
    sender = msg.get("From", "Unknown")
    reply_to = msg.get("Reply-To", None)
    received_headers = msg.get_all("Received", [])

    body = _extract_body(msg)
    links = _extract_links(body)
    sender_ip = _extract_sender_ip(received_headers)

    return {
        "subject": subject,
        "sender": sender,
        "reply_to": reply_to,
        "sender_ip": sender_ip,
        "body": body,
        "links": links,
        "received_headers": received_headers,
    }


def _decode_subject(subject: str) -> str:
    """
    Encoded email subjects ko readable text mein convert karta hai
    =?utf-8?q?...?= aur =?utf-8?b?...?= dono formats handle karta hai
    """
    try:
        decoded_parts = decode_header(subject)
        decoded_subject = ""
        for part, encoding in decoded_parts:
            if isinstance(part, bytes):
                decoded_subject += part.decode(
                    encoding or "utf-8", errors="ignore"
                )
            else:
                decoded_subject += str(part)
        return decoded_subject.strip()
    except Exception:
        return subject


def _extract_body(msg) -> str:
    """
    Email ke andar se actual text nikalta hai
    Multipart aur simple dono emails handle karta hai
    """
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition", ""))

            # Attachments skip karo
            if "attachment" in content_disposition:
                continue

            if content_type == "text/plain":
                try:
                    payload = part.get_payload(decode=True)
                    if payload:
                        body += payload.decode("utf-8", errors="ignore")
                except Exception:
                    pass

            # Agar plain text nahi mila toh HTML se try karo
            elif content_type == "text/html" and not body:
                try:
                    payload = part.get_payload(decode=True)
                    if payload:
                        html = payload.decode("utf-8", errors="ignore")
                        # HTML tags hata do basic regex se
                        body += re.sub(r'<[^>]+>', ' ', html)
                except Exception:
                    pass
    else:
        try:
            payload = msg.get_payload(decode=True)
            if payload:
                body = payload.decode("utf-8", errors="ignore")
            else:
                body = str(msg.get_payload())
        except Exception:
            body = str(msg.get_payload())

    return body.strip()


def _extract_links(text: str) -> List[str]:
    """
    Email body se saare links dhundta hai
    http aur https dono handle karta hai
    """
    url_pattern = re.compile(
        r'http[s]?://'
        r'(?:[a-zA-Z]|[0-9]|[$\-_@.&+!*\\(\\),]|(?:%[0-9a-fA-F]{2}))+'
    )
    links = url_pattern.findall(text)

    # Clean karo — trailing punctuation hata do
    cleaned = []
    for link in links:
        link = link.rstrip('.,;:)\'">')
        if len(link) > 10:  # bahut chote fake links skip karo
            cleaned.append(link)

    return list(set(cleaned))


def _extract_sender_ip(received_headers: List[str]) -> Optional[str]:
    """
    Email ke received headers se original sender IP dhundta hai
    Pehla non-private IP original sender hota hai
    """
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    for header in received_headers:
        ips = ip_pattern.findall(header)
        for ip in ips:
            if _is_valid_ip(ip) and not _is_private_ip(ip):
                return ip
    return None


def _is_valid_ip(ip: str) -> bool:
    """
    IP address valid hai ya nahi check karta hai
    0-255 range mein hona chahiye har octet
    """
    try:
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        return all(0 <= int(p) <= 255 for p in parts)
    except Exception:
        return False


def _is_private_ip(ip: str) -> bool:
    """
    Private/local IP addresses filter karta hai
    Ye IPs internal network ke hote hain, sender ke nahi
    """
    private_ranges = [
        "10.",
        "192.168.",
        "172.16.", "172.17.", "172.18.", "172.19.",
        "172.20.", "172.21.", "172.22.", "172.23.",
        "172.24.", "172.25.", "172.26.", "172.27.",
        "172.28.", "172.29.", "172.30.", "172.31.",
        "127.",
        "0.",
        "169.254.",  # link-local
        "::1",       # IPv6 localhost
    ]
    return any(ip.startswith(r) for r in private_ranges)