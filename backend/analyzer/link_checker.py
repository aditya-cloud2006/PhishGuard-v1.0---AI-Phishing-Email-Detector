import requests
import base64
from typing import Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import VIRUSTOTAL_API_KEY


def check_link_virustotal(url: str) -> Dict:
    if not VIRUSTOTAL_API_KEY or VIRUSTOTAL_API_KEY == "your_virustotal_key_here":
        return _mock_result(url)

    try:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        headers = {"x-apikey": VIRUSTOTAL_API_KEY}

        response = requests.get(
            f"https://www.virustotal.com/api/v3/urls/{url_id}",
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            stats = data["data"]["attributes"]["last_analysis_stats"]

            malicious = stats.get("malicious", 0)
            suspicious = stats.get("suspicious", 0)
            total = sum(stats.values())
            is_malicious = malicious > 0 or suspicious > 2

            if malicious > 5:
                verdict = "Confirmed Phishing"
            elif malicious > 0 or suspicious > 2:
                verdict = "Suspicious"
            else:
                verdict = "Clean"

            return {
                "url": url,
                "is_malicious": is_malicious,
                "detection_count": malicious + suspicious,
                "total_scanners": total,
                "verdict": verdict
            }

        elif response.status_code == 404:
            return _submit_url_for_scan(url)
        else:
            return _mock_result(url)

    except requests.exceptions.Timeout:
        return {
            "url": url, "is_malicious": False,
            "detection_count": 0, "total_scanners": 0,
            "verdict": "Timeout - manually check karo"
        }
    except Exception as e:
        return {
            "url": url, "is_malicious": False,
            "detection_count": 0, "total_scanners": 0,
            "verdict": f"Error: {str(e)}"
        }


def _submit_url_for_scan(url: str) -> Dict:
    try:
        headers = {
            "x-apikey": VIRUSTOTAL_API_KEY,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(
            "https://www.virustotal.com/api/v3/urls",
            headers=headers,
            data=f"url={url}",
            timeout=10
        )
        if response.status_code == 200:
            return {
                "url": url,
                "is_malicious": False,
                "detection_count": 0,
                "total_scanners": 0,
                "verdict": "Pehli baar scan hua - 1 min baad dobara check karo"
            }
    except Exception:
        pass
    return _mock_result(url)


def _mock_result(url: str) -> Dict:
    suspicious_keywords = [
        "login", "verify", "account", "secure", "update",
        "bank", "paypal", "amazon", "microsoft", "apple",
        "click", "confirm", "suspend", "urgent"
    ]
    url_lower = url.lower()
    found = [kw for kw in suspicious_keywords if kw in url_lower]
    is_suspicious = len(found) > 0

    return {
        "url": url,
        "is_malicious": is_suspicious,
        "detection_count": len(found),
        "total_scanners": 0,
        "verdict": f"Mock: {'Suspicious - ' + ', '.join(found) if found else 'Clean'}"
    }