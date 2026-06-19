import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from models.schemas import EmailAnalysisRequest, AnalysisReport
from analyzer.email_parser import parse_raw_email
from analyzer.link_checker import check_link_virustotal
from analyzer.ip_checker import check_ip_reputation
from analyzer.report import generate_report

app = FastAPI(
    title="PhishGuard API",
    description="AI-powered phishing email detection tool",
    version="1.0.0"
)

# CORS — frontend ko backend se baat karne deta hai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Frontend files serve karna
frontend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")


@app.get("/")
async def root():
    """Frontend serve karta hai"""
    index_path = os.path.join(frontend_path, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "PhishGuard API chal raha hai!", "docs": "/docs"}


@app.get("/health")
async def health_check():
    """Server theek se chal raha hai ya nahi check karta hai"""
    return {
        "status": "healthy",
        "message": "PhishGuard API ready hai"
    }


@app.post("/analyze", response_model=AnalysisReport)
async def analyze_email(request: EmailAnalysisRequest):
    """
    Main endpoint — email leta hai, analyze karta hai, report deta hai
    """
    # Step 1: Email parse karo
    if not request.raw_email or len(request.raw_email.strip()) < 10:
        raise HTTPException(
            status_code=400,
            detail="Email content bahut chota hai ya khali hai"
        )

    parsed = parse_raw_email(request.raw_email)

    if "error" in parsed:
        raise HTTPException(
            status_code=400,
            detail=f"Email parse nahi hua: {parsed['error']}"
        )

    # Step 2: Links check karo
    links = parsed.get("links", [])
    link_results = []
    for link in links[:5]:  # max 5 links check karo (API limit)
        result = check_link_virustotal(link)
        link_results.append(result)

    # Step 3: IP check karo
    sender_ip = parsed.get("sender_ip")
    ip_result = {}
    if sender_ip:
        ip_result = check_ip_reputation(sender_ip)

    # Step 4: Final report banao
    report = generate_report(parsed, link_results, ip_result)

    return report


@app.post("/analyze/quick")
async def quick_analyze(request: EmailAnalysisRequest):
    """
    Sirf email parse karta hai — links aur IP check nahi karta
    Fast result ke liye
    """
    parsed = parse_raw_email(request.raw_email)

    if "error" in parsed:
        raise HTTPException(status_code=400, detail=parsed["error"])

    return {
        "subject": parsed.get("subject"),
        "sender": parsed.get("sender"),
        "reply_to": parsed.get("reply_to"),
        "sender_ip": parsed.get("sender_ip"),
        "links_found": parsed.get("links", []),
        "links_count": len(parsed.get("links", []))
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)