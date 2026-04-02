# ---------------------------------------------------------
# Aqua-Alert: Working with Python Collections
# Milestone 4.15 - Lists, Tuples, and Dictionaries
# ---------------------------------------------------------

print("--- 1. Working with Python Lists (Ordered and Mutable) ---")
# Lists are ideal for data that needs to be updated, added, or removed.
active_alerts = ["Flash Flood", "Severe Thunderstorm", "Wind Advisory"]
print(f"Initial Alerts: {active_alerts}")

# Accessing elements using indexes
print(f"Primary threat today: {active_alerts[0]}")

# Modifying a list: Updating an existing item
active_alerts[2] = "High Wind Warning" # Replacing "Wind Advisory"
print(f"Updated Alerts (item replaced): {active_alerts}")

# Adding an item to the list
active_alerts.append("Extreme Heat")
print(f"Expanded Alerts (new alert added): {active_alerts}")

# Removing an item from the list
removed_alert = active_alerts.pop(0)
print(f"Alert Cleared: {removed_alert}")
print(f"Current Active Alerts: {active_alerts}\n")


print("--- 2. Working with Python Tuples (Ordered and Immutable) ---")
# Tuples are perfect for fixed data that should NOT change during execution.
# For example, geographic coordinates for a monitoring station.
STATION_COORDINATES = (34.0522, -118.2437) # (Latitude, Longitude)
print(f"Station Fixed Coordinates: {STATION_COORDINATES}")

# Accessing elements using indexes
print(f"Latitude: {STATION_COORDINATES[0]}")
print(f"Longitude: {STATION_COORDINATES[1]}")

# Demonstrating Immutability
print("\nAttempting to modify a tuple will raise an error:")
try:
    STATION_COORDINATES[0] = 35.0  # This will trigger a TypeError
except TypeError as e:
    print(f"-> Caught expected error: {e}")
print("Tuples are safer for constants like configuration values.\n")


print("--- 3. Working with Python Dictionaries (Key-Value Pairs) ---")
# Dictionaries model real-world entities effectively using descriptive keys.
district_status = {
    "name": "Riverside District",
    "population": 2450000,
    "current_rainfall_mm": 12.5,
    "active_warnings": True
}
print(f"District Metadata: {district_status}")

# Accessing values using keys
print(f"Monitoring Region: {district_status['name']}")
print(f"Current Status: {'Warnings Active' if district_status['active_warnings'] else 'All Clear'}")

# Modifying and adding key-value pairs
district_status["current_rainfall_mm"] += 5.0 # Update existing value
district_status["risk_level"] = "High"         # Add new key-value pair

print(f"Updated District Data: {district_status}")
print(f"Current Risk Level: {district_status['risk_level']}\n")


# ---------------------------------------------------------
# Scenario-Based Reasoning (For Video Walkthrough)
# ---------------------------------------------------------
"""
SCENARIO: 
You used a list to store configuration values that should never change, 
and a bug occurred because the list was modified accidentally.

QUESTION: 
What data structure would be more appropriate, and why?

ANSWER: 
A TUPLE would be more appropriate. 

WHY?
1. Immutability: Unlike lists, tuples cannot be changed after creation. If a developer 
   tries to 'append' or 'update' a value in a tuple, Python throws an error immediately.
2. Data Safety: This 'fail-fast' behavior prevents silent bugs where critical constants 
   are overwritten by mistake during program execution.
3. Intent: Using a tuple signals to other developers that the data is fixed and 
   should not be touched, making the code more readable and robust.
"""
