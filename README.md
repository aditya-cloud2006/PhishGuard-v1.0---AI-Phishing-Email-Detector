# 🛡️ PhishGuard — AI-Powered Phishing Email Detector

PhishGuard is a full-stack cybersecurity tool that analyzes suspicious emails for phishing indicators. It parses raw email content, checks embedded links against VirusTotal, verifies sender IP reputation via AbuseIPDB, and generates a comprehensive threat report with a confidence score.

## ✨ Features

- **Email Parsing** — Extracts subject, sender, reply-to, body, embedded links, and sender IP from raw email headers
- **Link Analysis** — Scans URLs against VirusTotal API for malicious content detection
- **IP Reputation Check** — Verifies sender IP against AbuseIPDB for abuse history
- **Phishing Score** — Calculates a 0–100 confidence score based on multiple threat signals
- **Red Flag Detection** — Identifies suspicious patterns:
  - Urgent/scam keywords in subject lines
  - Reply-To ≠ From mismatch
  - Malicious links
  - Bad IP reputation
  - Free email providers impersonating official organizations
- **Multi-Language Reports** — Supports English, Hindi, Hinglish, Marathi, Tamil, and Telugu
- **Mock Mode** — Works without API keys using keyword-based heuristic analysis

## 🏗️ Architecture

```
PhishGuard/
├── backend/
│   ├── main.py                  # FastAPI server & endpoints
│   ├── config.py                # Environment variable loader
│   ├── requirements.txt         # Python dependencies
│   ├── analyzer/
│   │   ├── email_parser.py      # Raw email parsing & link extraction
│   │   ├── link_checker.py      # VirusTotal URL scanning
│   │   ├── ip_checker.py        # AbuseIPDB IP reputation check
│   │   └── report.py            # Threat scoring & report generation
│   └── models/
│       └── schemas.py           # Pydantic request/response schemas
├── frontend/
│   ├── index.html               # Main UI
│   ├── style.css                # Styling
│   └── app.js                   # Frontend logic
├── sample_emails/
│   └── phishing_sample.eml      # Test phishing email
├── tests/
│   └── test_analyzer.py         # Unit tests
├── .env                         # API keys (not committed)
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aditya-cloud2006/Phisguard.git
   cd Phisguard
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Configure API keys** (optional — works without them in mock mode)
   
   Create a `.env` file in the project root:
   ```env
   VIRUSTOTAL_API_KEY=your_virustotal_key_here
   ABUSEIPDB_API_KEY=your_abuseipdb_key_here
   ```

   - Get a free VirusTotal API key: [virustotal.com](https://www.virustotal.com/)
   - Get a free AbuseIPDB API key: [abuseipdb.com](https://www.abuseipdb.com/)

5. **Run the server**
   ```bash
   cd backend
   python main.py
   ```

6. **Open in browser**
   ```
   http://localhost:8000
   ```

## 📡 API Endpoints

| Method | Endpoint         | Description                                    |
|--------|------------------|------------------------------------------------|
| GET    | `/`              | Serves the frontend UI                         |
| GET    | `/health`        | Health check                                   |
| POST   | `/analyze`       | Full analysis (email + links + IP)             |
| POST   | `/analyze/quick` | Quick parse only (no link/IP checks)           |
| GET    | `/docs`          | Interactive Swagger API documentation          |

### Example Request

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"raw_email": "From: hacker@gmail.com\nSubject: URGENT: Verify your account NOW\n\nClick here: http://fake-bank-login.com/verify"}'
```

## 🛠️ Tech Stack

| Component  | Technology                        |
|------------|-----------------------------------|
| Backend    | Python, FastAPI, Uvicorn          |
| Frontend   | HTML, CSS, JavaScript             |
| APIs       | VirusTotal v3, AbuseIPDB v2       |
| Validation | Pydantic, email-validator         |

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

**Built for real cybersecurity** 🔐
