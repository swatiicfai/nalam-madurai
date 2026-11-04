"""
Custom Tools for Nalam Madurai Swarm using Strands Agents SDK.
Decorated with @tool for automatic schema extraction and Bedrock LLM tool-calling.
"""

from typing import Dict, Any, List
try:
    from strands import tool
except ImportError:
    # Graceful fallback decorator for local preview/testing without SDK installed
    def tool(func):
        return func

from .hospital_data import MADURAI_UPHCS, GRH_MADURAI_DETAILS
from .schemes_data import TN_HEALTH_SCHEMES


@tool
def evaluate_triage_urgency(symptoms: str, duration_days: int = 1, is_emergency_sign: bool = False) -> Dict[str, Any]:
    """Evaluates the urgency level of patient symptoms and advises on safety steps in Tamil/English.

    Args:
        symptoms: Description of symptoms (e.g., chest pain, fever, breathless, fracture).
        duration_days: How many days the patient has experienced the symptoms.
        is_emergency_sign: Whether there are red-flag signs like fainting, severe bleeding, or acute chest pressure.

    Returns:
        Dict with urgency tier ('EMERGENCY_RED', 'URGENT_YELLOW', 'ROUTINE_GREEN'), recommended destination, emergency helpline, and Tamil instructions.
    """
    symptoms_lower = symptoms.lower()
    emergency_keywords = [
        "chest pain", "heart", "breathless", "accident", "bleeding", "stroke", "unconscious", "fits", "fracture",
        "நெஞ்சு", "மாரடைப்பு", "மூச்சு", "விபத்து", "மயக்கம்", "வலிப்பு", "ரத்தம்"
    ]
    
    is_red = is_emergency_sign or any(kw in symptoms_lower for kw in emergency_keywords)
    
    if is_red:
        return {
            "tier": "EMERGENCY_RED",
            "destination": "Government Rajaji Hospital (GRH) 24x7 Casualty & Trauma Center, Panagal Road, Goripalayam",
            "ambulance_call": "108 (Toll Free - Emergency Ambulance)",
            "action_advice_ta": "அவசர நிலை! உடனடியாக 108 ஆம்புலன்ஸை அழைக்கவும் அல்லது நேராக ராஜாஜி அரசு மருத்துவமனை (GRH) அவசர சிகிச்சைப் பிரிவிற்கு (Casualty) செல்லவும். எந்த தாமதமும் செய்ய வேண்டாம்.",
            "action_advice_en": "Medical emergency! Immediately call 108 ambulance or proceed to GRH Madurai 24x7 Trauma Casualty.",
            "grh_phone": GRH_MADURAI_DETAILS["emergency_phone"]
        }
    elif duration_days > 3 or "fever" in symptoms_lower or "pain" in symptoms_lower:
        return {
            "tier": "URGENT_YELLOW",
            "destination": "Nearest Madurai UPHC or GRH Main OPD Block",
            "recommended_timing": "Morning 8:00 AM - 11:30 AM",
            "action_advice_ta": "இது தீவிரமடைவதற்கு முன் உடனடியாக மருத்துவரை அணுகவும். காலையில் அருகில் உள்ள நகர்ப்புற ஆரம்ப சுகாதார நிலையம் (UPHC) அல்லது GRH புறநோயாளிகள் பிரிவிற்கு (OPD) செல்லவும்.",
            "action_advice_en": "Consult a doctor promptly. Visit your nearest Urban Primary Health Centre or GRH OPD in the morning session."
        }
    else:
        return {
            "tier": "ROUTINE_GREEN",
            "destination": "Local Ward Urban Primary Health Centre (UPHC)",
            "action_advice_ta": "பொதுவான உடல்நலக் கோளாறு. உங்கள் பகுதி ஆரம்ப சுகாதார நிலையத்திலேயே (UPHC) இலவச பரிசோதனை மற்றும் மாத்திரைகள் கிடைக்கும்.",
            "action_advice_en": "Routine checkup. Can be treated at your local ward UPHC without traveling far."
        }


@tool
def lookup_madurai_hospital_facility(condition_or_department: str, user_area: str = "Madurai") -> Dict[str, Any]:
    """Finds the correct department at Government Rajaji Hospital (GRH) or the closest Madurai Urban PHC.

    Args:
        condition_or_department: Medical department needed or condition (e.g., Cardiology, Maternity, Child care, Bone, General Medicine).
        user_area: User's location in Madurai (e.g., Sellur, K.Pudur, Goripalayam, Teppakulam, Periyar).

    Returns:
        Specific GRH building wing, floor, OPD schedule, and nearby UPHC options.
    """
    query = condition_or_department.lower()
    matched_dept = None

    dept_mappings = [
        (["cardio", "heart", "இதயம்", "நெஞ்சு"], "Cardiology & Cath Lab"),
        (["neuro", "brain", "தலை", "நரம்பு"], "Neurology & Neurosurgery"),
        (["maternity", "delivery", "pregnant", "கர்ப்பிணி", "பிரசவம்", "பெண்கள்"], "Obstetrics & Gynaecology (Maternity Ward)"),
        (["bone", "fracture", "ortho", "எலும்பு", "முறிவு"], "Orthopaedics & Bone Fractures"),
        (["child", "pediatric", "baby", "குழந்தை"], "Paediatrics (Child Care)"),
        (["fever", "cough", "general", "காய்ச்சல்", "சளி", "பொது"], "General Medicine & Fever Clinic")
    ]

    for keywords, dept_name in dept_mappings:
        if any(kw in query for kw in keywords):
            for dept in GRH_MADURAI_DETAILS["departments"]:
                if dept["name"] == dept_name:
                    matched_dept = dept
                    break
            if matched_dept:
                break
            
    if not matched_dept:
        matched_dept = GRH_MADURAI_DETAILS["departments"][-1]  # General Medicine
        
    # Match nearby UPHC
    area_query = user_area.lower()
    matched_uphcs = [u for u in MADURAI_UPHCS if u["area"].lower().split()[0] in area_query]
    if not matched_uphcs:
        matched_uphcs = MADURAI_UPHCS[:2]

    return {
        "grh_facility": {
            "hospital_name": GRH_MADURAI_DETAILS["official_name"],
            "location": GRH_MADURAI_DETAILS["location"],
            "landmark": GRH_MADURAI_DETAILS["landmark"],
            "department": matched_dept["name"],
            "building_location": matched_dept["building"],
            "opd_hours": matched_dept["opd_days"],
            "scheme_coverage": matched_dept["coverage"],
            "bus_route_info": GRH_MADURAI_DETAILS["how_to_reach"]
        },
        "nearby_local_uphcs": matched_uphcs,
        "tamil_navigation_note": f"ராஜாஜி மருத்துவமனையில் {matched_dept['name']} பிரிவு {matched_dept['building']}-ல் இயங்குகிறது. காலை 8 மணி முதல் 12 மணி வரை டோக்கன் பெறலாம்."
    }


@tool
def verify_tamilnadu_health_scheme(condition_or_need: str, has_smart_ration_card: bool = True) -> Dict[str, Any]:
    """Verifies eligibility and document checklists for Tamil Nadu healthcare schemes like CMCHIS, Nammai Kaakkum 48, and Makkalai Thedi Maruthuvam.

    Args:
        condition_or_need: The healthcare need (e.g., surgery, heart bypass, accident emergency, BP/Sugar home medicines, pregnancy delivery).
        has_smart_ration_card: Whether the family holds a Tamil Nadu Smart Family Card (Ration Card).

    Returns:
        Applicable scheme name, coverage limit, required proof documents, and Madurai helpdesk counter.
    """
    need = condition_or_need.lower()
    
    if any(k in need for k in ["accident", "road", "trauma", "emergency", "விபத்து"]):
        scheme = TN_HEALTH_SCHEMES[1]  # Nammai Kaakkum 48
    elif any(k in need for k in ["sugar", "diabetes", "bp", "hypertension", "home medicine", "மக்களைத் தேடி"]):
        scheme = TN_HEALTH_SCHEMES[2]  # Makkalai Thedi Maruthuvam
    elif any(k in need for k in ["pregnant", "delivery", "baby", "maternity", "பிரசவம்"]):
        scheme = TN_HEALTH_SCHEMES[3]  # Muthulakshmi Reddy
    else:
        scheme = TN_HEALTH_SCHEMES[0]  # CMCHIS

    return {
        "scheme_name_tamil": scheme.get("name_ta"),
        "scheme_name_english": scheme.get("name_en"),
        "coverage_benefit": scheme.get("coverage_amount"),
        "eligibility_criteria": scheme.get("eligibility"),
        "documents_required": scheme.get("documents_needed", []),
        "grh_helpdesk": scheme.get("grh_helpdesk", "GRH Main Entrance Reception"),
        "is_eligible_with_smart_card": True if has_smart_ration_card else "Check income certificate at Madurai Collectorate/e-Sevai center",
        "tamil_guidance": f"நீங்கள் '{scheme.get('name_ta')}' மூலம் பயன்பெறலாம். பலன்: {scheme.get('coverage_amount')}."
    }
