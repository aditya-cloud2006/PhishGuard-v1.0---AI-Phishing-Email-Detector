import requests
from typing import Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import ABUSEIPDB_API_KEY


def check_ip_reputation(ip_address: str) -> Dict:
    if not ip_address:
        return {"error": "IP address nahi mila"}

    if not ABUSEIPDB_API_KEY or ABUSEIPDB_API_KEY == "your_abuseipdb_key_here":
        return _mock_ip_result(ip_address)

    try:
        headers = {
            "Key": ABUSEIPDB_API_KEY,
            "Accept": "application/json"
        }
        params = {
            "ipAddress": ip_address,
            "maxAgeInDays": 90
        }

        response = requests.get(
            "https://api.abuseipdb.com/api/v2/check",
            headers=headers,
            params=params,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()["data"]

            abuse_score = data.get("abuseConfidenceScore", 0)
            country = data.get("countryCode", "Unknown")
            isp = data.get("isp", "Unknown")
            total_reports = data.get("totalReports", 0)

            if abuse_score >= 80:
                verdict = "Highly Malicious IP"
            elif abuse_score >= 40:
                verdict = "Suspicious IP"
            elif abuse_score >= 10:
                verdict = "Low Risk"
            else:
                verdict = "Clean IP"

            return {
                "ip_address": ip_address,
                "abuse_score": abuse_score,
                "country": country,
                "isp": isp,
                "total_reports": total_reports,
                "verdict": verdict
            }
        else:
            return _mock_ip_result(ip_address)

    except Exception as e:
        return {
            "ip_address": ip_address,
            "abuse_score": 0,
            "country": "Unknown",
            "isp": "Unknown",
            "verdict": f"Check failed: {str(e)}"
        }


def _mock_ip_result(ip: str) -> Dict:
    return {
        "ip_address": ip,
        "abuse_score": 0,
        "country": "Unknown",
        "isp": "API key nahi hai - abuseipdb.com pe register karo",
        "verdict": "Manual check required"
    }