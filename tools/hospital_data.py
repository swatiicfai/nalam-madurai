"""
Madurai Healthcare Facilities & GRH (Government Rajaji Hospital) Directory
Authoritative grounding data for Madurai district public healthcare navigation.
"""

MADURAI_UPHCS = [
    {
        "name": "Sellur Urban Primary Health Centre (UPHC)",
        "area": "Sellur / Goripalayam",
        "distance_from_periyar_bus_stand_km": 3.5,
        "timing": "8:00 AM - 12:00 PM, 4:00 PM - 8:00 PM",
        "services": ["General OPD", "Maternal Care", "Immunization", "Makkalai Thedi Maruthuvam Drug Refills", "Basic Lab tests"],
        "emergency": False
    },
    {
        "name": "K. Pudur Urban Primary Health Centre",
        "area": "K. Pudur / Surveyor Colony",
        "distance_from_periyar_bus_stand_km": 5.0,
        "timing": "8:00 AM - 12:00 PM, 4:00 PM - 8:00 PM",
        "services": ["General OPD", "Diabetes & BP screening", "Antenatal checks", "Pharmacy"],
        "emergency": False
    },
    {
        "name": "Teppakulam UPHC",
        "area": "Teppakulam / Anuppanadi",
        "distance_from_periyar_bus_stand_km": 4.2,
        "timing": "8:00 AM - 12:00 PM, 4:00 PM - 8:00 PM",
        "services": ["General OPD", "Pediatric Care", "Fever Clinic", "Free Lab Diagnostics"],
        "emergency": False
    },
    {
        "name": "Villapuram UPHC",
        "area": "Villapuram / Avaniyapuram Road",
        "distance_from_periyar_bus_stand_km": 4.8,
        "timing": "8:00 AM - 12:00 PM, 4:00 PM - 8:00 PM",
        "services": ["General Medicine", "NCD Screening", "Postnatal Care"],
        "emergency": False
    },
    {
        "name": "Munichalai UPHC",
        "area": "Munichalai / Nelpettai",
        "distance_from_periyar_bus_stand_km": 2.2,
        "timing": "8:00 AM - 12:00 PM, 4:00 PM - 8:00 PM",
        "services": ["General OPD", "Fever clinic", "Vaccinations"],
        "emergency": False
    }
]

GRH_MADURAI_DETAILS = {
    "official_name": "Government Rajaji Hospital (GRH) & Madurai Medical College",
    "location": "Panagal Road, Shenoy Nagar / Goripalayam, Madurai - 625020",
    "landmark": "Near Goripalayam Dargah / Vaigai River Bridge",
    "emergency_phone": "0452-2532535 / 108",
    "toll_free_health_helpline": "104",
    "casualty_trauma": {
        "status": "24x7 Open",
        "building": "Tower Block Ground Floor (Casualty & Trauma Care Centre)",
        "free_emergency_care": "Innuyir Kaappom - Nammai Kaakkum 48 applies automatically for accident victims"
    },
    "opd_timings": "7:30 AM to 12:00 PM (Monday to Saturday)",
    "departments": [
        {
            "name": "Cardiology & Cath Lab",
            "building": "Super Speciality Block (Trauma Care side), 2nd Floor",
            "opd_days": "Monday to Saturday (8:00 AM - 12:00 PM)",
            "coverage": "CMCHIS / Free Government Health Scheme eligible"
        },
        {
            "name": "Neurology & Neurosurgery",
            "building": "Super Speciality Block, 3rd Floor",
            "opd_days": "Monday to Saturday",
            "coverage": "CMCHIS covered"
        },
        {
            "name": "Obstetrics & Gynaecology (Maternity Ward)",
            "building": "Old Wing Maternity Block (Opposite GRH Main Gate)",
            "opd_days": "24x7 Delivery & Antenatal care daily",
            "coverage": "Muthulakshmi Reddy Scheme cash assistance + Nutrition kit"
        },
        {
            "name": "Orthopaedics & Bone Fractures",
            "building": "Main Block Ground & First Floor",
            "opd_days": "Monday to Saturday",
            "coverage": "Free implants under CMCHIS"
        },
        {
            "name": "Paediatrics (Child Care)",
            "building": "Institute of Child Health (ICH), Near Anna Bus Stand / Shenoy Nagar",
            "opd_days": "24x7 Emergency, OPD 8:00 AM - 1:00 PM",
            "coverage": "Completely free under RBSK"
        },
        {
            "name": "General Medicine & Fever Clinic",
            "building": "Main OPD Block, Ground Floor",
            "opd_days": "Daily 7:30 AM - 12:00 PM",
            "coverage": "Free medicines at central pharmacy counter"
        }
    ],
    "how_to_reach": "Frequent city buses from Periyar Bus Stand (Bus 77, 48, 23 series to Goripalayam), Mattuthavani MGR Bus Stand (Bus 24, 48, 77 to Goripalayam)."
}
