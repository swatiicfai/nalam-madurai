"""
Tamil Nadu Government Health Schemes Knowledge Base
Authoritative details for CMCHIS, Nammai Kaakkum 48, Makkalai Thedi Maruthuvam, and Maternity assistance.
"""

TN_HEALTH_SCHEMES = [
    {
        "id": "cmchis",
        "name_en": "Chief Minister's Comprehensive Health Insurance Scheme (CMCHIS)",
        "name_ta": "முதலமைச்சரின் விரிவான மருத்துவக் காப்பீட்டுத் திட்டம் (CMCHIS)",
        "coverage_amount": "Up to ₹5,00,000 per family per year",
        "eligibility": "Annual family income below ₹1,20,000 as per Ration Card / Smart Card, or recognized unorganized workers / destitute.",
        "documents_needed": [
            "Smart Ration Card (ஸ்மார்ட் குடும்ப அட்டை)",
            "Aadhaar Card (ஆதார் அட்டை)",
            "Income Certificate (வருமானச் சான்றிதழ் from VAO/Tahsildar if not printed on ration card)",
            "Doctor recommendation letter / GRH OPD slip"
        ],
        "grh_helpdesk": "GRH Madurai Main Entrance CMCHIS Kiosk (Counters 4 & 5)",
        "toll_free": "1800-425-3993"
    },
    {
        "id": "nammai_kaakkum_48",
        "name_en": "Innuyir Kaappom - Nammai Kaakkum 48 (Road Accident Emergency Care)",
        "name_ta": "இன்னுயிர் காப்போம் - நம்மை காக்கும் 48 திட்டம்",
        "coverage_amount": "Free medical & surgical treatment up to ₹1,00,000 for the first 48 hours",
        "eligibility": "Universal! Anyone injured in a road accident in Tamil Nadu (regardless of income, domicile, or state of origin).",
        "documents_needed": ["No pre-documentation required at the time of emergency admission. Just reach GRH Casualty or recognized empanelled hospital."],
        "key_message": "விபத்து நடந்த முதல் 48 மணி நேரத்தில் கட்டணமில்லா சிகிச்சை. ஆவணங்கள் எதுவும் தேவையில்லை."
    },
    {
        "id": "makkalai_thedi_maruthuvam",
        "name_en": "Makkalai Thedi Maruthuvam (Healthcare at Doorsteps)",
        "name_ta": "மக்களைத் தேடி மருத்துவம் திட்டம்",
        "coverage_amount": "Doorstep delivery of chronic medicines & screening",
        "eligibility": "Hypertension (BP), Diabetes, Dialysis patients, and Palliative care patients aged 45+ or bedridden.",
        "services": [
            "Monthly BP and Diabetes medicines delivered directly to home",
            "Dialysis kits for chronic kidney disease patients",
            "Physiotherapy for post-stroke patients at home"
        ],
        "how_to_avail": "Contact your nearest Madurai Urban Primary Health Centre (UPHC) or village Health Sub-centre."
    },
    {
        "id": "muthulakshmi_reddy",
        "name_en": "Dr. Muthulakshmi Reddy Maternity Benefit Scheme (MRMBS)",
        "name_ta": "டாக்டர் முத்துலட்சுமி ரெட்டி மகப்பேறு நிதி உதவித் திட்டம்",
        "coverage_amount": "₹18,000 total assistance (₹14,000 cash in installments + ₹4,000 nutrition kits)",
        "eligibility": "Pregnant mothers delivering in government hospitals (like GRH Madurai or local UPHCs).",
        "documents_needed": [
            "RCH ID (PICME registration number from nearest PHC)",
            "Aadhaar card",
            "Mother's bank passbook (Aadhaar-linked)",
            "Smart Ration card"
        ]
    }
]
