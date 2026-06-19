const API_URL = "http://localhost:8000";

// =====================
// UI TRANSLATIONS
// =====================
const UI_TEXT = {
    english: {
        title: "PhishGuard — Email Threat Analyzer",
        header_brand: "PhishGuard",
        header_tagline: "AI-Powered Phishing Email Detector",
        section_title: "Analyze Your Email",
        section_subtitle: "Paste the complete suspicious email content below",
        textarea_placeholder: `Paste email here...

Example:
From: support@gmail.com
To: you@company.com
Subject: URGENT: Your account will be suspended
Reply-To: hacker123@gmail.com
Received: from 185.234.219.208

Dear Customer,
Click here immediately: http://fake-bank-login.com/verify`,
        btn_analyze: "🔍 Analyze",
        btn_clear: "🗑️ Clear",
        btn_sample: "📧 Load Sample Email",
        btn_analyzing: "⏳ Analyzing...",
        loading_text: "Analyzing email...",
        email_details: "📧 Email Details",
        ip_analysis: "🌐 IP Analysis",
        label_subject: "Subject:",
        label_sender: "Sender:",
        label_sender_ip: "Sender IP:",
        label_ip: "IP:",
        label_country: "Country:",
        label_isp: "ISP:",
        label_abuse_score: "Abuse Score:",
        label_verdict: "Verdict:",
        red_flags_title: "🚩 Red Flags Found",
        no_red_flags: "✅ No red flags found",
        links_title: "🔗 Links Analysis",
        no_links: "No links found in email",
        no_ip: "IP not found",
        footer: "PhishGuard v1.0 — Built for real cybersecurity",
        lang_label: "🌐 Report Language:",
        alert_empty: "Please paste an email first!",
        alert_short: "Email content too short. Please paste complete email.",
        alert_no_server: "❌ Backend server not found!\n\nRun in VS Code terminal:\ncd backend\npython main.py",
        verdict_phishing: "PHISHING EMAIL!",
        verdict_suspicious: "SUSPICIOUS EMAIL",
        verdict_safe: "Looks Safe",
        confidence: "Confidence Score",
    },
    hinglish: {
        title: "PhishGuard — Email Threat Analyzer",
        header_brand: "PhishGuard",
        header_tagline: "AI-Powered Phishing Email Detector",
        section_title: "Email Analyze Karo",
        section_subtitle: "Suspicious email ka poora content neeche paste karo",
        textarea_placeholder: `Yahan email paste karo...

Example:
From: support@gmail.com
To: you@company.com
Subject: URGENT: Your account will be suspended
Reply-To: hacker123@gmail.com
Received: from 185.234.219.208

Dear Customer,
Click here immediately: http://fake-bank-login.com/verify`,
        btn_analyze: "🔍 Analyze Karo",
        btn_clear: "🗑️ Clear",
        btn_sample: "📧 Sample Email Load Karo",
        btn_analyzing: "⏳ Analyzing...",
        loading_text: "Email analyze ho rahi hai...",
        email_details: "📧 Email Details",
        ip_analysis: "🌐 IP Analysis",
        label_subject: "Subject:",
        label_sender: "Sender:",
        label_sender_ip: "Sender IP:",
        label_ip: "IP:",
        label_country: "Country:",
        label_isp: "ISP:",
        label_abuse_score: "Abuse Score:",
        label_verdict: "Verdict:",
        red_flags_title: "🚩 Red Flags Mile",
        no_red_flags: "✅ Koi red flags nahi mile",
        links_title: "🔗 Links Analysis",
        no_links: "Koi links nahi mile email mein",
        no_ip: "IP nahi mila",
        footer: "PhishGuard v1.0 — Built for real cybersecurity",
        lang_label: "🌐 Report Language:",
        alert_empty: "Pehle email paste karo!",
        alert_short: "Email content bahut chota hai. Poora email paste karo.",
        alert_no_server: "❌ Backend server nahi mila!\n\nVS Code terminal mein ye chalaao:\ncd backend\npython main.py",
        verdict_phishing: "PHISHING EMAIL HAI!",
        verdict_suspicious: "SUSPICIOUS EMAIL",
        verdict_safe: "Safe Lagta Hai",
        confidence: "Confidence Score",
    },
    hindi: {
        title: "PhishGuard — ईमेल खतरा विश्लेषक",
        header_brand: "PhishGuard",
        header_tagline: "AI-संचालित फ़िशिंग ईमेल डिटेक्टर",
        section_title: "ईमेल विश्लेषण करें",
        section_subtitle: "संदिग्ध ईमेल का पूरा कंटेंट नीचे पेस्ट करें",
        textarea_placeholder: "यहाँ ईमेल पेस्ट करें...",
        btn_analyze: "🔍 विश्लेषण करें",
        btn_clear: "🗑️ साफ़ करें",
        btn_sample: "📧 नमूना ईमेल लोड करें",
        btn_analyzing: "⏳ विश्लेषण हो रहा है...",
        loading_text: "ईमेल का विश्लेषण हो रहा है...",
        email_details: "📧 ईमेल विवरण",
        ip_analysis: "🌐 IP विश्लेषण",
        label_subject: "विषय:",
        label_sender: "भेजने वाला:",
        label_sender_ip: "भेजने वाले का IP:",
        label_ip: "IP:",
        label_country: "देश:",
        label_isp: "ISP:",
        label_abuse_score: "दुरुपयोग स्कोर:",
        label_verdict: "निर्णय:",
        red_flags_title: "🚩 संदिग्ध संकेत मिले",
        no_red_flags: "✅ कोई संदिग्ध संकेत नहीं मिले",
        links_title: "🔗 लिंक विश्लेषण",
        no_links: "ईमेल में कोई लिंक नहीं मिला",
        no_ip: "IP नहीं मिला",
        footer: "PhishGuard v1.0 — वास्तविक साइबर सुरक्षा के लिए",
        lang_label: "🌐 रिपोर्ट भाषा:",
        alert_empty: "पहले ईमेल पेस्ट करें!",
        alert_short: "ईमेल कंटेंट बहुत छोटा है। पूरा ईमेल पेस्ट करें।",
        alert_no_server: "❌ बैकएंड सर्वर नहीं मिला!\n\nटर्मिनल में चलाएं:\ncd backend\npython main.py",
        verdict_phishing: "फ़िशिंग ईमेल है!",
        verdict_suspicious: "संदिग्ध ईमेल",
        verdict_safe: "सुरक्षित लगता है",
        confidence: "विश्वास स्कोर",
    },
    marathi: {
        title: "PhishGuard — ईमेल धोका विश्लेषक",
        header_brand: "PhishGuard",
        header_tagline: "AI-चालित फिशिंग ईमेल डिटेक्टर",
        section_title: "ईमेल तपासा",
        section_subtitle: "संशयास्पद ईमेलचा संपूर्ण मजकूर खाली पेस्ट करा",
        textarea_placeholder: "येथे ईमेल पेस्ट करा...",
        btn_analyze: "🔍 तपासा",
        btn_clear: "🗑️ साफ करा",
        btn_sample: "📧 नमुना ईमेल लोड करा",
        btn_analyzing: "⏳ तपासत आहे...",
        loading_text: "ईमेल तपासत आहे...",
        email_details: "📧 ईमेल तपशील",
        ip_analysis: "🌐 IP विश्लेषण",
        label_subject: "विषय:",
        label_sender: "पाठवणारा:",
        label_sender_ip: "पाठवणाऱ्याचा IP:",
        label_ip: "IP:",
        label_country: "देश:",
        label_isp: "ISP:",
        label_abuse_score: "गैरवापर स्कोर:",
        label_verdict: "निकाल:",
        red_flags_title: "🚩 संशयास्पद संकेत आढळले",
        no_red_flags: "✅ कोणतेही संशयास्पद संकेत नाहीत",
        links_title: "🔗 लिंक विश्लेषण",
        no_links: "ईमेलमध्ये कोणतेही लिंक नाहीत",
        no_ip: "IP आढळला नाही",
        footer: "PhishGuard v1.0 — वास्तविक सायबर सुरक्षेसाठी",
        lang_label: "🌐 अहवाल भाषा:",
        alert_empty: "आधी ईमेल पेस्ट करा!",
        alert_short: "ईमेल मजकूर खूप लहान आहे. संपूर्ण ईमेल पेस्ट करा.",
        alert_no_server: "❌ बॅकएंड सर्व्हर सापडला नाही!\n\nटर्मिनलमध्ये चालवा:\ncd backend\npython main.py",
        verdict_phishing: "फिशिंग ईमेल आहे!",
        verdict_suspicious: "संशयास्पद ईमेल",
        verdict_safe: "सुरक्षित वाटते",
        confidence: "विश्वास स्कोर",
    },
    tamil: {
        title: "PhishGuard — மின்னஞ்சல் அச்சுறுத்தல் பகுப்பாய்வி",
        header_brand: "PhishGuard",
        header_tagline: "AI-இயக்கும் ஃபிஷிங் மின்னஞ்சல் கண்டறிவி",
        section_title: "மின்னஞ்சலை பகுப்பாய்வு செய்",
        section_subtitle: "சந்தேகமான மின்னஞ்சலின் முழு உள்ளடக்கத்தை கீழே ஒட்டவும்",
        textarea_placeholder: "இங்கே மின்னஞ்சல் ஒட்டவும்...",
        btn_analyze: "🔍 பகுப்பாய்வு செய்",
        btn_clear: "🗑️ அழி",
        btn_sample: "📧 மாதிரி மின்னஞ்சல் ஏற்று",
        btn_analyzing: "⏳ பகுப்பாய்வு நடக்கிறது...",
        loading_text: "மின்னஞ்சல் பகுப்பாய்வு நடக்கிறது...",
        email_details: "📧 மின்னஞ்சல் விவரங்கள்",
        ip_analysis: "🌐 IP பகுப்பாய்வு",
        label_subject: "பொருள்:",
        label_sender: "அனுப்புநர்:",
        label_sender_ip: "அனுப்புநர் IP:",
        label_ip: "IP:",
        label_country: "நாடு:",
        label_isp: "ISP:",
        label_abuse_score: "துஷ்பிரயோக மதிப்பெண்:",
        label_verdict: "தீர்ப்பு:",
        red_flags_title: "🚩 சந்தேக அறிகுறிகள்",
        no_red_flags: "✅ சந்தேக அறிகுறிகள் இல்லை",
        links_title: "🔗 இணைப்பு பகுப்பாய்வு",
        no_links: "மின்னஞ்சலில் இணைப்புகள் இல்லை",
        no_ip: "IP கிடைக்கவில்லை",
        footer: "PhishGuard v1.0 — உண்மையான இணைய பாதுகாப்பிற்காக",
        lang_label: "🌐 அறிக்கை மொழி:",
        alert_empty: "முதலில் மின்னஞ்சல் ஒட்டவும்!",
        alert_short: "மின்னஞ்சல் உள்ளடக்கம் மிகவும் சிறியது.",
        alert_no_server: "❌ பின்தள சேவையகம் கிடைக்கவில்லை!\n\nடெர்மினலில் இயக்கவும்:\ncd backend\npython main.py",
        verdict_phishing: "ஃபிஷிங் மின்னஞ்சல்!",
        verdict_suspicious: "சந்தேகமான மின்னஞ்சல்",
        verdict_safe: "பாதுகாப்பானது போல் தெரிகிறது",
        confidence: "நம்பிக்கை மதிப்பெண்",
    },
    telugu: {
        title: "PhishGuard — ఇమెయిల్ ముప్పు విశ్లేషకుడు",
        header_brand: "PhishGuard",
        header_tagline: "AI-ఆధారిత ఫిషింగ్ ఇమెయిల్ డిటెక్టర్",
        section_title: "ఇమెయిల్ విశ్లేషించండి",
        section_subtitle: "అనుమానాస్పద ఇమెయిల్ యొక్క పూర్తి కంటెంట్ క్రింద పేస్ట్ చేయండి",
        textarea_placeholder: "ఇక్కడ ఇమెయిల్ పేస్ట్ చేయండి...",
        btn_analyze: "🔍 విశ్లేషించండి",
        btn_clear: "🗑️ క్లియర్",
        btn_sample: "📧 నమూనా ఇమెయిల్ లోడ్ చేయండి",
        btn_analyzing: "⏳ విశ్లేషిస్తోంది...",
        loading_text: "ఇమెయిల్ విశ్లేషిస్తోంది...",
        email_details: "📧 ఇమెయిల్ వివరాలు",
        ip_analysis: "🌐 IP విశ్లేషణ",
        label_subject: "విషయం:",
        label_sender: "పంపినవారు:",
        label_sender_ip: "పంపినవారి IP:",
        label_ip: "IP:",
        label_country: "దేశం:",
        label_isp: "ISP:",
        label_abuse_score: "దుర్వినియోగ స్కోర్:",
        label_verdict: "తీర్పు:",
        red_flags_title: "🚩 అనుమానాస్పద సంకేతాలు",
        no_red_flags: "✅ అనుమానాస్పద సంకేతాలు లేవు",
        links_title: "🔗 లింక్ విశ్లేషణ",
        no_links: "ఇమెయిల్‌లో లింక్‌లు లేవు",
        no_ip: "IP దొరకలేదు",
        footer: "PhishGuard v1.0 — నిజమైన సైబర్ భద్రత కోసం",
        lang_label: "🌐 నివేదిక భాష:",
        alert_empty: "ముందు ఇమెయిల్ పేస్ట్ చేయండి!",
        alert_short: "ఇమెయిల్ కంటెంట్ చాలా చిన్నది. పూర్తి ఇమెయిల్ పేస్ట్ చేయండి.",
        alert_no_server: "❌ బ్యాకెండ్ సర్వర్ దొరకలేదు!\n\nటెర్మినల్‌లో రన్ చేయండి:\ncd backend\npython main.py",
        verdict_phishing: "ఫిషింగ్ ఇమెయిల్!",
        verdict_suspicious: "అనుమానాస్పద ఇమెయిల్",
        verdict_safe: "సురక్షితంగా కనిపిస్తోంది",
        confidence: "నమ్మకం స్కోర్",
    },
};

const SAMPLE_EMAIL = `From: security-alert@gmail.com
To: employee@yourcompany.com
Subject: URGENT: Your account will be suspended in 24 hours
Reply-To: collect.data123@gmail.com
Received: from 185.234.219.208 (unknown) by mail.server.com
Date: Thu, 19 Jun 2025 10:30:00 +0530
Message-ID: <fake123@gmail.com>

Dear Valued Customer,

We have detected suspicious activity on your account.
Your account will be SUSPENDED immediately unless you verify now.

Click here to verify your account: http://secure-login-verify.tk/amazon/login
Or visit: http://paypal-account-update.ml/verify?user=you

This is URGENT. Act within 24 hours or lose access permanently.

Security Team
Amazon Customer Support`;


// =====================
// LANGUAGE FUNCTIONS
// =====================

function getCurrentLang() {
    return document.getElementById("langSelect").value || "english";
}

function t(key) {
    const lang = getCurrentLang();
    return UI_TEXT[lang]?.[key] || UI_TEXT["english"][key] || key;
}

function applyLanguage() {
    const lang = getCurrentLang();
    const tx = UI_TEXT[lang] || UI_TEXT["english"];

    // Page title
    document.title = tx.title;

    // Header
    document.querySelector(".brand").textContent = tx.header_brand;
    document.querySelector(".tagline").textContent = tx.header_tagline;

    // Section
    document.querySelector(".input-section h2").textContent = tx.section_title;
    document.querySelector(".subtitle").textContent = tx.section_subtitle;

    // Textarea placeholder
    document.getElementById("emailInput").placeholder = tx.textarea_placeholder;

    // Buttons
    document.getElementById("analyzeBtn").textContent = tx.btn_analyze;
    document.getElementById("clearBtn").textContent = tx.btn_clear;
    document.getElementById("sampleBtn").textContent = tx.btn_sample;

    // Loading
    document.querySelector(".loading p").textContent = tx.loading_text;

    // Labels - Email Details
    document.querySelector(".lang-selector label").textContent = tx.lang_label;
    document.querySelector("#emailDetailsTitle").textContent = tx.email_details;
    document.querySelector("#ipAnalysisTitle").textContent = tx.ip_analysis;
    document.querySelector("#labelSubject").textContent = tx.label_subject;
    document.querySelector("#labelSender").textContent = tx.label_sender;
    document.querySelector("#labelSenderIP").textContent = tx.label_sender_ip;
    document.querySelector("#labelIP").textContent = tx.label_ip;
    document.querySelector("#labelCountry").textContent = tx.label_country;
    document.querySelector("#labelISP").textContent = tx.label_isp;
    document.querySelector("#labelAbuseScore").textContent = tx.label_abuse_score;
    document.querySelector("#labelVerdict").textContent = tx.label_verdict;

    // Section titles
    document.querySelector("#redFlagsTitle").textContent = tx.red_flags_title;
    document.querySelector("#linksTitle").textContent = tx.links_title;

    // Footer
    document.querySelector("footer p").textContent = tx.footer;
}


// =====================
// MAIN FUNCTIONS
// =====================

async function analyzeEmail() {
    const emailInput = document.getElementById("emailInput").value.trim();

    if (!emailInput) {
        alert(t("alert_empty"));
        return;
    }
    if (emailInput.length < 20) {
        alert(t("alert_short"));
        return;
    }

    setLoading(true);
    hideResults();

    try {
        const response = await fetch(`${API_URL}/analyze`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                raw_email: emailInput,
                language: getCurrentLang()
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || "Server error aaya");
        }

        const data = await response.json();
        displayResults(data);

    } catch (error) {
        if (error.message.includes("fetch")) {
            alert(t("alert_no_server"));
        } else {
            alert(`❌ Error: ${error.message}`);
        }
    } finally {
        setLoading(false);
    }
}


function displayResults(data) {
    const tx = UI_TEXT[getCurrentLang()] || UI_TEXT["english"];

    // Verdict Card
    const verdictCard = document.getElementById("verdictCard");
    const verdictIcon = document.getElementById("verdictIcon");
    const verdictTitle = document.getElementById("verdictTitle");
    const verdictScore = document.getElementById("verdictScore");

    verdictCard.className = "verdict-card";

    if (data.is_phishing) {
        if (data.confidence_score >= 75) {
            verdictCard.classList.add("phishing");
            verdictIcon.textContent = "🚨";
            verdictTitle.textContent = tx.verdict_phishing;
        } else {
            verdictCard.classList.add("suspicious");
            verdictIcon.textContent = "⚠️";
            verdictTitle.textContent = tx.verdict_suspicious;
        }
    } else {
        verdictCard.classList.add("safe");
        verdictIcon.textContent = "✅";
        verdictTitle.textContent = tx.verdict_safe;
    }

    verdictScore.textContent = `${tx.confidence}: ${data.confidence_score}/100`;

    // Recommendation
    document.getElementById("recommendationText").textContent = data.recommendation;

    // Email Details
    document.getElementById("detailSubject").textContent = data.subject || "N/A";
    document.getElementById("detailSender").textContent = data.sender_email || "N/A";
    document.getElementById("detailIP").textContent = data.sender_ip || tx.no_ip;

    // IP Analysis
    if (data.ip_analysis && !data.ip_analysis.error && data.ip_analysis.ip_address) {
        document.getElementById("ipAddress").textContent = data.ip_analysis.ip_address || "N/A";
        document.getElementById("ipCountry").textContent = data.ip_analysis.country || "Unknown";
        document.getElementById("ipISP").textContent = data.ip_analysis.isp || "Unknown";
        document.getElementById("ipScore").textContent = `${data.ip_analysis.abuse_score}/100`;
        document.getElementById("ipVerdict").textContent = data.ip_analysis.verdict || "N/A";
        document.getElementById("ipCard").classList.remove("hidden");
    } else {
        document.getElementById("ipCard").classList.add("hidden");
    }

    // Red Flags
    const redFlagsList = document.getElementById("redFlagsList");
    redFlagsList.innerHTML = "";

    if (data.red_flags && data.red_flags.length > 0) {
        data.red_flags.forEach(flag => {
            const li = document.createElement("li");
            li.textContent = flag;
            redFlagsList.appendChild(li);
        });
    } else {
        const li = document.createElement("li");
        li.textContent = tx.no_red_flags;
        li.style.color = "#4caf50";
        li.style.background = "#0a1a0a";
        li.style.border = "1px solid #2d5a2d";
        redFlagsList.appendChild(li);
    }

    // Links Analysis
    const linksList = document.getElementById("linksList");
    linksList.innerHTML = "";

    if (data.suspicious_links && data.suspicious_links.length > 0) {
        data.suspicious_links.forEach(link => {
            const div = document.createElement("div");
            div.className = `link-item ${link.is_malicious ? "malicious" : "clean"}`;
            div.innerHTML = `
                <div class="link-url">${link.url}</div>
                <div class="link-verdict">
                    ${link.is_malicious ? "🚨" : "✅"} ${link.verdict}
                    ${link.total_scanners > 0 ?
                        `<span style="color:#546e7a; font-weight:normal">
                            (${link.detection_count}/${link.total_scanners} engines)
                        </span>` : ""}
                </div>
            `;
            linksList.appendChild(div);
        });
    } else {
        linksList.innerHTML = `<p style="color:#546e7a; font-size:13px">${tx.no_links}</p>`;
    }

    document.getElementById("resultSection").classList.remove("hidden");
    document.getElementById("resultSection").scrollIntoView({
        behavior: "smooth", block: "start"
    });
}


function setLoading(show) {
    const loading = document.getElementById("loading");
    const analyzeBtn = document.getElementById("analyzeBtn");
    const tx = UI_TEXT[getCurrentLang()] || UI_TEXT["english"];

    if (show) {
        loading.classList.remove("hidden");
        analyzeBtn.disabled = true;
        analyzeBtn.textContent = tx.btn_analyzing;
    } else {
        loading.classList.add("hidden");
        analyzeBtn.disabled = false;
        analyzeBtn.textContent = tx.btn_analyze;
    }
}

function hideResults() {
    document.getElementById("resultSection").classList.add("hidden");
}

function clearAll() {
    document.getElementById("emailInput").value = "";
    hideResults();
    document.getElementById("emailInput").focus();
}

function loadSample() {
    document.getElementById("emailInput").value = SAMPLE_EMAIL;
    document.getElementById("emailInput").focus();
}

// Language change hone pe poora UI update karo
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("langSelect").addEventListener("change", () => {
        applyLanguage();
        hideResults();
    });
    applyLanguage();
});