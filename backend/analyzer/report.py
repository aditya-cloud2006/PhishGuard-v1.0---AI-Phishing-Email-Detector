from typing import Dict, List

TRANSLATIONS = {
    "english": {
        "urgent_subject": "Suspicious words found in subject",
        "reply_to_trick": "Reply-To is different from From — classic phishing trick",
        "from_label": "From",
        "reply_to_label": "Reply-To",
        "malicious_links": "malicious link(s) found",
        "ip_malicious": "Sender IP is highly malicious",
        "ip_suspicious": "Sender IP is suspicious",
        "ip_score": "score",
        "ip_country": "country",
        "free_email_claim": "Free email provider claiming to be official organization",
        "sender_label": "Sender",
        "rec_block": "🚨 BLOCK THIS EMAIL — High confidence phishing. Do not click any links.",
        "rec_suspicious": "⚠️ SUSPICIOUS — Report to IT admin. Do not take any action.",
        "rec_low_risk": "🔍 LOW RISK — Some suspicious elements found. Verify sender directly.",
        "rec_safe": "✅ LOOKS SAFE — Still avoid clicking unknown links.",
    },
    "hindi": {
        "urgent_subject": "विषय में संदिग्ध शब्द मिले",
        "reply_to_trick": "Reply-To अलग है From से — फ़िशिंग की पहचान",
        "from_label": "भेजने वाला",
        "reply_to_label": "Reply-To",
        "malicious_links": "खतरनाक लिंक मिले",
        "ip_malicious": "भेजने वाले का IP बेहद खतरनाक है",
        "ip_suspicious": "भेजने वाले का IP संदिग्ध है",
        "ip_score": "स्कोर",
        "ip_country": "देश",
        "free_email_claim": "मुफ़्त ईमेल से आधिकारिक संस्था होने का दावा",
        "sender_label": "भेजने वाला",
        "rec_block": "🚨 इस ईमेल को ब्लॉक करें — यह फ़िशिंग ईमेल है। किसी भी लिंक पर क्लिक न करें।",
        "rec_suspicious": "⚠️ संदिग्ध — IT एडमिन को रिपोर्ट करें। कोई कार्रवाई न करें।",
        "rec_low_risk": "🔍 कम जोखिम — कुछ संदिग्ध तत्व मिले। भेजने वाले से सीधे पुष्टि करें।",
        "rec_safe": "✅ सुरक्षित लगता है — फिर भी अज्ञात लिंक पर क्लिक करने से बचें।",
    },
    "hinglish": {
        "urgent_subject": "Subject mein suspicious words mile",
        "reply_to_trick": "Reply-To alag hai From se — classic phishing trick",
        "from_label": "From",
        "reply_to_label": "Reply-To",
        "malicious_links": "malicious link(s) mila",
        "ip_malicious": "Sender IP highly malicious hai",
        "ip_suspicious": "Sender IP suspicious hai",
        "ip_score": "score",
        "ip_country": "country",
        "free_email_claim": "Free email se official organization hone ka claim",
        "sender_label": "Sender",
        "rec_block": "🚨 BLOCK KARO — High confidence phishing email hai. Koi bhi link click mat karo.",
        "rec_suspicious": "⚠️ SUSPICIOUS — IT admin ko report karo, khud kuch mat karo.",
        "rec_low_risk": "🔍 LOW RISK — Kuch suspicious elements hain. Sender ko directly verify karo.",
        "rec_safe": "✅ SAFE LAGTA HAI — Phir bhi unknown links pe click karne se bachna.",
    },
    "marathi": {
        "urgent_subject": "विषयात संशयास्पद शब्द आढळले",
        "reply_to_trick": "Reply-To वेगळे आहे From पेक्षा — फिशिंगची ओळख",
        "from_label": "पाठवणारा",
        "reply_to_label": "Reply-To",
        "malicious_links": "धोकादायक लिंक आढळल्या",
        "ip_malicious": "पाठवणाऱ्याचा IP अत्यंत धोकादायक आहे",
        "ip_suspicious": "पाठवणाऱ्याचा IP संशयास्पद आहे",
        "ip_score": "स्कोर",
        "ip_country": "देश",
        "free_email_claim": "मोफत ईमेलवरून अधिकृत संस्था असल्याचा दावा",
        "sender_label": "पाठवणारा",
        "rec_block": "🚨 हा ईमेल ब्लॉक करा — हे फिशिंग आहे. कोणत्याही लिंकवर क्लिक करू नका.",
        "rec_suspicious": "⚠️ संशयास्पद — IT व्यवस्थापकाला कळवा. स्वतः काहीही करू नका.",
        "rec_low_risk": "🔍 कमी धोका — काही संशयास्पद घटक आढळले. पाठवणाऱ्याची थेट पुष्टी करा.",
        "rec_safe": "✅ सुरक्षित वाटते — तरीही अज्ञात लिंकवर क्लिक करणे टाळा.",
    },
    "tamil": {
        "urgent_subject": "பொருளில் சந்தேகமான வார்த்தைகள் கண்டறியப்பட்டன",
        "reply_to_trick": "Reply-To மற்றும் From வேறுபட்டது — ஃபிஷிங் அறிகுறி",
        "from_label": "அனுப்புநர்",
        "reply_to_label": "Reply-To",
        "malicious_links": "தீங்கான இணைப்புகள் கண்டறியப்பட்டன",
        "ip_malicious": "அனுப்புநரின் IP மிகவும் ஆபத்தானது",
        "ip_suspicious": "அனுப்புநரின் IP சந்தேகமானது",
        "ip_score": "மதிப்பெண்",
        "ip_country": "நாடு",
        "free_email_claim": "இலவச மின்னஞ்சலில் இருந்து அதிகாரப்பூர்வ நிறுவனம் என்று கூறுகிறது",
        "sender_label": "அனுப்புநர்",
        "rec_block": "🚨 இந்த மின்னஞ்சலை தடு — இது ஃபிஷிங். எந்த இணைப்பையும் கிளிக் செய்யாதே.",
        "rec_suspicious": "⚠️ சந்தேகமானது — IT நிர்வாகிக்கு தெரிவி. நீயே எதுவும் செய்யாதே.",
        "rec_low_risk": "🔍 குறைந்த ஆபத்து — சில சந்தேக அம்சங்கள் உள்ளன. அனுப்புநரை நேரடியாக சரிபார்.",
        "rec_safe": "✅ பாதுகாப்பானது போல் தெரிகிறது — இருப்பினும் தெரியாத இணைப்புகளை கிளிக் செய்யாதே.",
    },
    "telugu": {
        "urgent_subject": "విషయంలో అనుమానాస్పద పదాలు కనుగొనబడ్డాయి",
        "reply_to_trick": "Reply-To మరియు From వేర్వేరుగా ఉన్నాయి — ఫిషింగ్ సంకేతం",
        "from_label": "పంపినవారు",
        "reply_to_label": "Reply-To",
        "malicious_links": "హానికరమైన లింక్‌లు కనుగొనబడ్డాయి",
        "ip_malicious": "పంపినవారి IP చాలా ప్రమాదకరమైనది",
        "ip_suspicious": "పంపినవారి IP అనుమానాస్పదంగా ఉంది",
        "ip_score": "స్కోర్",
        "ip_country": "దేశం",
        "free_email_claim": "ఉచిత ఇమెయిల్ నుండి అధికారిక సంస్థ అని పేర్కొంటోంది",
        "sender_label": "పంపినవారు",
        "rec_block": "🚨 ఈ ఇమెయిల్‌ను బ్లాక్ చేయండి — ఇది ఫిషింగ్. ఏ లింక్‌పై క్లిక్ చేయవద్దు.",
        "rec_suspicious": "⚠️ అనుమానాస్పదం — IT నిర్వాహకుడికి నివేదించండి. మీరే ఏమీ చేయవద్దు.",
        "rec_low_risk": "🔍 తక్కువ ప్రమాదం — కొన్ని అనుమానాస్పద అంశాలు కనుగొనబడ్డాయి. పంపినవారిని నేరుగా ధృవీకరించండి.",
        "rec_safe": "✅ సురక్షితంగా కనిపిస్తోంది — అయినప్పటికీ తెలియని లింక్‌లను క్లిక్ చేయవద్దు.",
    },
}


def generate_report(
    parsed_email: Dict,
    link_results: List[Dict],
    ip_result: Dict,
    language: str = "english"
) -> Dict:

    # Language fallback
    lang = language.lower()
    if lang not in TRANSLATIONS:
        lang = "english"
    t = TRANSLATIONS[lang]

    red_flags = []
    phishing_score = 0

    subject = parsed_email.get("subject", "")
    sender = parsed_email.get("sender", "")
    reply_to = parsed_email.get("reply_to")

    # Check 1: Subject mein urgent keywords
    urgent_words = [
        "urgent", "immediately", "account suspended", "verify now",
        "action required", "winner", "prize", "click here",
        "limited time", "expire", "blocked", "alert", "warning"
    ]
    subject_lower = subject.lower()
    found_urgent = [w for w in urgent_words if w in subject_lower]
    if found_urgent:
        red_flags.append(
            f"{t['urgent_subject']}: {', '.join(found_urgent)}"
        )
        phishing_score += 20

    # Check 2: Reply-To alag hai From se
    if reply_to and reply_to.strip() != sender.strip():
        red_flags.append(
            f"{t['reply_to_trick']}\n"
            f"  {t['from_label']}: {sender}\n"
            f"  {t['reply_to_label']}: {reply_to}"
        )
        phishing_score += 30

    # Check 3: Malicious links
    malicious_links = [l for l in link_results if l.get("is_malicious")]
    if malicious_links:
        red_flags.append(
            f"{len(malicious_links)} {t['malicious_links']}:\n"
            f"  {malicious_links[0]['url'][:60]}... → {malicious_links[0]['verdict']}"
        )
        phishing_score += 40

    # Check 4: IP reputation
    if ip_result and not ip_result.get("error"):
        abuse_score = ip_result.get("abuse_score", 0)
        if abuse_score >= 80:
            red_flags.append(
                f"{t['ip_malicious']} "
                f"({t['ip_score']}: {abuse_score}/100, "
                f"{t['ip_country']}: {ip_result.get('country')})"
            )
            phishing_score += 40
        elif abuse_score >= 40:
            red_flags.append(
                f"{t['ip_suspicious']} ({t['ip_score']}: {abuse_score}/100)"
            )
            phishing_score += 20

    # Check 5: Free email se official hone ka claim
    free_providers = [
        "gmail.com", "yahoo.com", "hotmail.com",
        "outlook.com", "ymail.com"
    ]
    official_claims = [
        "bank", "sbi", "hdfc", "icici", "amazon",
        "microsoft", "apple", "paypal", "support",
        "noreply", "security"
    ]
    sender_lower = sender.lower()
    uses_free = any(p in sender_lower for p in free_providers)
    claims_official = any(
        o in sender_lower or o in subject_lower
        for o in official_claims
    )
    if uses_free and claims_official:
        red_flags.append(
            f"{t['free_email_claim']}\n"
            f"  {t['sender_label']}: {sender}"
        )
        phishing_score += 25

    # Score cap
    phishing_score = min(phishing_score, 100)
    is_phishing = phishing_score >= 50

    # Recommendation
    if phishing_score >= 75:
        recommendation = t["rec_block"]
    elif phishing_score >= 50:
        recommendation = t["rec_suspicious"]
    elif phishing_score >= 25:
        recommendation = t["rec_low_risk"]
    else:
        recommendation = t["rec_safe"]

    return {
        "is_phishing": is_phishing,
        "confidence_score": phishing_score,
        "subject": subject,
        "sender_email": sender,
        "sender_ip": parsed_email.get("sender_ip"),
        "suspicious_links": link_results,
        "ip_analysis": ip_result,
        "red_flags": red_flags,
        "recommendation": recommendation,
        "language": lang
    }