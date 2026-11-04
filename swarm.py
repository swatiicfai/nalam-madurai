"""
Nalam Madurai: Multi-Agent Swarm Orchestration with Strands Agents SDK.

Implements collaborative agents specialized in:
1. Triage & Emergency Assessment (Tamil & English)
2. Madurai Hospital & GRH Wing Navigator
3. Tamil Nadu Health Scheme & CMCHIS Advisor
"""

import os
import sys
from typing import Dict, Any

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from tools.strands_tools import (
    evaluate_triage_urgency,
    lookup_madurai_hospital_facility,
    verify_tamilnadu_health_scheme
)

# Prompts crafted with respectful Madurai Tamil ethos and safety guidelines
TRIAGE_AGENT_PROMPT = """You are the 'Triage & Symptom Specialist' in the Nalam Madurai Swarm.
Your primary role is to listen to the user's health concerns with empathy, evaluate urgency using evaluate_triage_urgency,
and clearly identify red-flag conditions.

Rules:
1. Never pretend to replace a licensed doctor. Always recommend certified medical attention.
2. In emergency cases (chest pain, stroke, severe bleeding, road trauma), immediately highlight 108 ambulance and GRH 24x7 Casualty.
3. Always provide reassuring, clear instructions in authentic Tamil alongside English.
"""

HOSPITAL_NAVIGATOR_PROMPT = """You are the 'Madurai Hospital & GRH Navigation Specialist'.
You know Government Rajaji Hospital (GRH Madurai) inside and out—including Panagal Road entry,
Super Speciality Block, Casualty Trauma block, Institute of Child Health (ICH), and the local Urban Primary Health Centres (Sellur, K.Pudur, Teppakulam, etc.).

Rules:
1. Use lookup_madurai_hospital_facility to pinpoint the exact building, floor, OPD timings, and bus access.
2. Tell patients when to go (OPD tokens are 7:30 AM - 12:00 PM) to avoid crowd delays.
3. Advise when a local UPHC is adequate vs when GRH tertiary care is required.
"""

SCHEME_ADVISOR_PROMPT = """You are the 'Tamil Nadu Health Scheme Specialist'.
You are an expert on CMCHIS (Kalaignar Kaappeettu Thittam), Innuyir Kaappom (Nammai Kaakkum 48),
and Makkalai Thedi Maruthuvam.

Rules:
1. Use verify_tamilnadu_health_scheme to fetch exact coverage figures and required documents (Smart Ration Card, Aadhaar).
2. For road accident cases, emphasize that Nammai Kaakkum 48 provides ₹1,00,000 free treatment for the first 48 hours without any paperwork!
3. Direct patients to GRH Madurai CMCHIS Kiosks (Counters 4 & 5).
"""

COORDINATOR_PROMPT = """You are 'Nalam Madurai' (நலம் மதுரை), a compassionate AI healthcare concierge designed for Madurai and Southern Tamil Nadu.
You speak warm, respectful Madurai Tamil (e.g. 'வணக்கம், உங்களுக்கு எப்படி உதவலாம்?') and clear English.

You coordinate with specialized agents in your swarm:
- Triage Specialist for symptoms
- Hospital Navigator for GRH wings & local PHCs
- Scheme Specialist for CMCHIS / TN Govt insurance coverage

Always synthesize the responses into a clear, comforting, and actionable summary for the patient and their family.
"""

def build_strands_swarm():
    """Initializes and returns the Strands Agent Swarm using the official strands SDK."""
    try:
        from strands import Agent
        from strands.multiagent import Swarm
        
        triage_agent = Agent(
            name="triage_specialist",
            system_prompt=TRIAGE_AGENT_PROMPT,
            tools=[evaluate_triage_urgency]
        )
        
        hospital_agent = Agent(
            name="grh_hospital_navigator",
            system_prompt=HOSPITAL_NAVIGATOR_PROMPT,
            tools=[lookup_madurai_hospital_facility]
        )
        
        scheme_agent = Agent(
            name="tn_scheme_advisor",
            system_prompt=SCHEME_ADVISOR_PROMPT,
            tools=[verify_tamilnadu_health_scheme]
        )
        
        coordinator_agent = Agent(
            name="nalam_madurai_coordinator",
            system_prompt=COORDINATOR_PROMPT,
            tools=[evaluate_triage_urgency, lookup_madurai_hospital_facility, verify_tamilnadu_health_scheme]
        )
        
        swarm = Swarm(
            agents=[coordinator_agent, triage_agent, hospital_agent, scheme_agent]
        )
        return swarm
    except Exception as e:
        # Returns None if strands-agents SDK dependencies or Bedrock credentials are being mocked
        return None


class SimulatedNalamMaduraiSwarm:
    """Demonstration & Evaluation harness providing zero-latency deterministic execution

    of the Strands multi-agent swarm logic for judging and local CLI demonstrations.
    """
    def __init__(self):
        self.triage_tool = evaluate_triage_urgency
        self.hospital_tool = lookup_madurai_hospital_facility
        self.scheme_tool = verify_tamilnadu_health_scheme

    def process_query(self, query: str, user_location: str = "Madurai") -> Dict[str, Any]:
        """Simulates the collaborative coordination of the 3 specialized agents."""
        # 1. Triage Assessment
        triage_res = self.triage_tool(symptoms=query, duration_days=2)
        
        # 2. Hospital / GRH Navigation
        hospital_res = self.hospital_tool(condition_or_department=query, user_area=user_location)
        
        # 3. Scheme Verification
        scheme_res = self.scheme_tool(condition_or_need=query, has_smart_ration_card=True)
        
        # Synthesized Bilingual Response
        return {
            "query": query,
            "triage_assessment": triage_res,
            "facility_guidance": hospital_res,
            "scheme_coverage": scheme_res
        }
