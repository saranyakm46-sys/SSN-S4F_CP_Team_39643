import csv

# Data - Large dataset of AI tools for wildlife conservation
data = [
    {"Year": 2021, "AI_Tool": "Camera Traps with AI", "Purpose": "Monitor wildlife", "ML/AI_Algorithm": "Image Recognition", "Eco_Guard_Role": "Deploy & Monitor", "Impact": "Reduced poaching by 20%"},
    {"Year": 2021, "AI_Tool": "Drones with AI", "Purpose": "Patrol forests", "ML/AI_Algorithm": "Object Detection", "Eco_Guard_Role": "Operate drones", "Impact": "Improved area coverage"},
    {"Year": 2021, "AI_Tool": "Acoustic Sensors", "Purpose": "Detect animal calls", "ML/AI_Algorithm": "Sound Classification", "Eco_Guard_Role": "Maintain sensors", "Impact": "Better species tracking"},
    {"Year": 2021, "AI_Tool": "Satellite Imagery Analysis", "Purpose": "Forest cover monitoring", "ML/AI_Algorithm": "Image Segmentation", "Eco_Guard_Role": "Validate alerts", "Impact": "Prevented illegal logging"},
    {"Year": 2022, "AI_Tool": "Predictive Poaching Alerts", "Purpose": "Prevent poaching", "ML/AI_Algorithm": "Predictive Modeling", "Eco_Guard_Role": "Patrol high-risk zones", "Impact": "Decreased poaching incidents"},
    {"Year": 2022, "AI_Tool": "Wildlife Tracking Collars", "Purpose": "Monitor animal movement", "ML/AI_Algorithm": "GPS Data Analysis", "Eco_Guard_Role": "Attach collars & monitor", "Impact": "Improved migration data"},
    {"Year": 2022, "AI_Tool": "AI-Powered Rangers App", "Purpose": "Real-time reporting", "ML/AI_Algorithm": "Mobile AI Analytics", "Eco_Guard_Role": "Report sightings", "Impact": "Faster incident response"},
    {"Year": 2022, "AI_Tool": "Thermal Imaging Cameras", "Purpose": "Night patrol monitoring", "ML/AI_Algorithm": "Thermal Detection", "Eco_Guard_Role": "Night surveillance", "Impact": "Enhanced night safety"},
    {"Year": 2023, "AI_Tool": "Illegal Activity Detection AI", "Purpose": "Detect logging/poaching", "ML/AI_Algorithm": "Anomaly Detection", "Eco_Guard_Role": "Act on alerts", "Impact": "Reduced illegal activities"},
    {"Year": 2023, "AI_Tool": "AI-Powered Species ID", "Purpose": "Identify species from photos", "ML/AI_Algorithm": "Image Classification", "Eco_Guard_Role": "Capture & label photos", "Impact": "Faster species cataloging"},
    {"Year": 2023, "AI_Tool": "Drone Swarm Patrols", "Purpose": "Cover large areas quickly", "ML/AI_Algorithm": "Swarm Coordination AI", "Eco_Guard_Role": "Control drones", "Impact": "Improved area surveillance"},
    {"Year": 2023, "AI_Tool": "AI Poacher Behavior Analysis", "Purpose": "Predict poacher movement", "ML/AI_Algorithm": "Behavior Modeling", "Eco_Guard_Role": "Strategic patrolling", "Impact": "Proactive anti-poaching"},
    {"Year": 2024, "AI_Tool": "Wildfire Detection AI", "Purpose": "Detect forest fires early", "ML/AI_Algorithm": "Satellite Image Analysis", "Eco_Guard_Role": "Respond quickly", "Impact": "Reduced fire damage"},
    {"Year": 2024, "AI_Tool": "AI-Enhanced Biodiversity Mapping", "Purpose": "Map species diversity", "ML/AI_Algorithm": "Data Analytics", "Eco_Guard_Role": "Collect field data", "Impact": "Better conservation planning"},
    {"Year": 2024, "AI_Tool": "Illegal Fishing Detection AI", "Purpose": "Monitor rivers/lakes", "ML/AI_Algorithm": "Object Detection", "Eco_Guard_Role": "Intervene & report", "Impact": "Reduced illegal fishing"},
    {"Year": 2024, "AI_Tool": "AI-Powered Poacher Tracking", "Purpose": "Monitor illegal activities", "ML/AI_Algorithm": "Predictive Analytics", "Eco_Guard_Role": "Plan patrols", "Impact": "Higher poacher apprehension"},
    {"Year": 2024, "AI_Tool": "Smart Sensor Networks", "Purpose": "Track environmental changes", "ML/AI_Algorithm": "Sensor Data Analysis", "Eco_Guard_Role": "Maintain sensors", "Impact": "Early habitat threat detection"},
    {"Year": 2025, "AI_Tool": "AI Camera Traps for Rare Species", "Purpose": "Monitor endangered species", "ML/AI_Algorithm": "Deep Learning", "Eco_Guard_Role": "Deploy & monitor cameras", "Impact": "Better endangered species data"},
    {"Year": 2025, "AI_Tool": "AI Habitat Mapping", "Purpose": "Map wildlife habitats", "ML/AI_Algorithm": "GIS + ML", "Eco_Guard_Role": "Field validation", "Impact": "Improved habitat protection"},
    {"Year": 2025, "AI_Tool": "AI-Powered Poaching Risk Maps", "Purpose": "Predict high-risk areas", "ML/AI_Algorithm": "Spatial Analysis", "Eco_Guard_Role": "Patrol prioritization", "Impact": "Focused anti-poaching efforts"},
    {"Year": 2025, "AI_Tool": "AI Wildlife Crime Reporting", "Purpose": "Real-time crime reporting", "ML/AI_Algorithm": "Mobile AI + NLP", "Eco_Guard_Role": "Report incidents", "Impact": "Faster law enforcement response"},
    {"Year": 2025, "AI_Tool": "AI Drone Patrol Coordination", "Purpose": "Manage multiple drones", "ML/AI_Algorithm": "Swarm AI", "Eco_Guard_Role": "Drone control & monitoring", "Impact": "Maximized area coverage"},
    {"Year": 2025, "AI_Tool": "AI Animal Health Monitoring", "Purpose": "Monitor wildlife health", "ML/AI_Algorithm": "Predictive Health Analytics", "Eco_Guard_Role": "Collect health data", "Impact": "Early disease detection"},
]

# CSV file name
filename = "ai_wildlife_conservation_super_large.csv"

# Writing to CSV
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ["Year", "AI_Tool", "Purpose", "ML/AI_Algorithm", "Eco_Guard_Role", "Impact"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"Super large CSV file '{filename}' ready with {len(data)} entries!")
