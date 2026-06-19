from pydantic import BaseModel
from typing import Optional, List


class EmailAnalysisRequest(BaseModel):
    raw_email: str
    sender_email: Optional[str] = None
    language: Optional[str] = "english"


class LinkResult(BaseModel):
    url: str
    is_malicious: bool
    detection_count: int
    total_scanners: int
    verdict: str


class IPResult(BaseModel):
    ip_address: str
    abuse_score: int
    country: str
    isp: str
    verdict: str


class AnalysisReport(BaseModel):
    is_phishing: bool
    confidence_score: int
    sender_email: Optional[str]
    sender_ip: Optional[str]
    subject: Optional[str]
    suspicious_links: List[LinkResult]
    ip_analysis: Optional[IPResult]
    red_flags: List[str]
    recommendation: str
    language: Optional[str] = "english"