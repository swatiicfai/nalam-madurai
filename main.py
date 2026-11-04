"""
Main Interactive Demo for 'Nalam Madurai' (நலம் மதுரை)
AWS User Group Madurai - Strands SDK Hackathon
"""

import os
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Ensure current project directory is in python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

import json
from swarm import build_strands_swarm, SimulatedNalamMaduraiSwarm

SAMPLE_MADURAI_SCENARIOS = [
    {
        "title": "Scenario 1: Chest Discomfort & Emergency at Goripalayam",
        "query": "ஐயா, எனக்கு நேற்றிலிருந்து நெஞ்சு பாரமாகவும் மூச்சு திணறலாகவும் இருக்கிறது. ராஜாஜி ஆஸ்பத்திரில எந்த வார்டுக்கு போகணும்? காப்பீடு அட்டை செல்லுமா?",
        "location": "Goripalayam"
    },
    {
        "title": "Scenario 2: Motherhood & Delivery Navigation",
        "query": "கர்ப்பிணி பெண்ணுக்கு பிரசவம் பார்க்க ராஜாஜி மருத்துவமனையில் எந்த பிளாக்குக்கு செல்ல வேண்டும்? முத்துலட்சுமி ரெட்டி திட்ட உதவி எப்படி பெறுவது?",
        "location": "Sellur"
    },
    {
        "title": "Scenario 3: Road Accident Trauma & Instant Care",
        "query": "மதுரை பைபாஸ் ரோட்டில் பைக் விபத்து. பலத்த காயம். உடனடியாக என்ன செய்ய வேண்டும்? காப்பீடு கார்டு கையில் இல்லை.",
        "location": "Mattuthavani"
    },
    {
        "title": "Scenario 4: Elderly Diabetes & BP Medication at Doorstep",
        "query": "எங்கள் தாத்தாவுக்கு சர்க்கரை மற்றும் ரத்தக் கொதிப்பு உள்ளது. வீட்டின் அருகிலேயே மாத்திரைகள் பெற 'மக்களைத் தேடி மருத்துவம்' திட்டம் எவ்வாறு உதவும்?",
        "location": "K. Pudur"
    }
]

def print_banner():
    banner = r"""
========================================================================
     நலம் மதுரை (NALAM MADURAI) - HEALTHCARE CONCIERGE SWARM
        Built with Strands Agents SDK & Amazon Bedrock
     For AWS User Group Madurai Hackathon (Social Good Track)
========================================================================
    """
    print(banner)

def render_result(res: dict):
    print("\n" + "-"*70)
    print(f"📌 வினவல் (Query): {res['query']}")
    print("-"*70)
    
    triage = res["triage_assessment"]
    tier = triage.get("tier")
    tier_badge = "🔴 [அவசர நிலை / EMERGENCY]" if tier == "EMERGENCY_RED" else "🟡 [முக்கியம் / URGENT]" if tier == "URGENT_YELLOW" else "🟢 [பொதுவானது / ROUTINE]"
    print(f"\n🩺 [Triage Specialist Agent] நிலை: {tier_badge}")
    print(f"   தமிழ் வழிகாட்டுதல் : {triage.get('action_advice_ta')}")
    print(f"   English Guidance    : {triage.get('action_advice_en')}")
    print(f"   பரிந்துரைக்கப்பட்ட இடம்: {triage.get('destination')}")
    if triage.get("ambulance_call"):
        print(f"   🚨 ஆம்புலன்ஸ் எண்    : {triage.get('ambulance_call')}")
    
    facility = res["facility_guidance"]["grh_facility"]
    print(f"\n🏥 [GRH Hospital Navigator Agent]")
    print(f"   மருத்துவமனை       : {facility.get('hospital_name')}")
    print(f"   பிரிவு & கட்டிடம்    : {facility.get('department')} -> {facility.get('building_location')}")
    print(f"   நேரம் (OPD Hours)   : {facility.get('opd_hours')}")
    print(f"   பேருந்து வழி (Buses): {facility.get('bus_route_info')}")
    
    scheme = res["scheme_coverage"]
    print(f"\n💳 [TN Scheme Specialist Agent]")
    print(f"   பொருந்தும் திட்டம்   : {scheme.get('scheme_name_tamil')} ({scheme.get('scheme_name_english')})")
    print(f"   காப்பீட்டுத் தொகை   : {scheme.get('coverage_benefit')}")
    print(f"   தேவையான ஆவணங்கள்   : {', '.join(scheme.get('documents_required', []))}")
    print(f"   உதவி மையம்         : {scheme.get('grh_helpdesk')}")
    print("="*70 + "\n")

def run_scenarios():
    print_banner()
    swarm = SimulatedNalamMaduraiSwarm()
    
    print("\n🚀 Running 4 Authentic Madurai Healthcare Scenarios:\n")
    for idx, sc in enumerate(SAMPLE_MADURAI_SCENARIOS, 1):
        print(f"\n▶ [{sc['title']}]")
        result = swarm.process_query(sc["query"], sc["location"])
        render_result(result)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        print_banner()
        swarm = SimulatedNalamMaduraiSwarm()
        print("Type your query in Tamil or English (or type 'exit' to quit):")
        while True:
            try:
                user_input = input("\nஉரையாடலைத் தொடங்கவும் (Ask Nalam Madurai) > ")
                if user_input.strip().lower() in ["exit", "quit", "q"]:
                    break
                if not user_input.strip():
                    continue
                res = swarm.process_query(user_input)
                render_result(res)
            except (KeyboardInterrupt, EOFError):
                break
    else:
        run_scenarios()
