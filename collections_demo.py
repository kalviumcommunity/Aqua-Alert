# ---------------------------------------------------------
# Aqua-Alert: Python Collections Demonstration
# (Lists, Tuples, and Dictionaries)
# ---------------------------------------------------------

# --- Part 1: Python Lists ---
# Lists are ordered, mutable collections used for related items.
monitored_districts = ["Riverside", "Orange County", "Palm Springs", "San Diego"]

print("--- Lists: Monitored Districts ---")
print(f"Original list: {monitored_districts}")
print(f"Accessed second element (Index 1): {monitored_districts[1]}")

# Modifying an existing list item
monitored_districts[2] = "Coachella Valley"
# Adding a new item
monitored_districts.append("Inland Empire")

print(f"Updated list: {monitored_districts}\n")


# --- Part 2: Python Tuples ---
# Tuples are ordered, immutable collections used for fixed constants.
alert_severity_levels = ("Low", "Moderate", "High", "Critical")

print("--- Tuples: Alert Severity Levels ---")
print(f"Severity Levels: {alert_severity_levels}")
print(f"First severity level: {alert_severity_levels[0]}")

# Python Tuples are immutable, so the following would cause a TypeError:
# alert_severity_levels[0] = "Minimal"  # Uncommenting this will raise an Error

print("Attempting to modify a tuple will raise a TypeError: 'tuple' object does not support item assignment\n")


# --- Part 3: Python Dictionaries ---
# Dictionaries are key-value pairs used for mapping meaningful relations.
district_status = {
    "Riverside": "Critical",
    "Orange County": "High",
    "San Diego": "Moderate"
}

print("--- Dictionaries: District Alerts ---")
print(f"Full dictionary: {district_status}")

# Accessing a value by its key
current_status = district_status["Riverside"]
print(f"Current Alert in Riverside: {current_status}")

# Modifying a value in the dictionary
district_status["San Diego"] = "High"
# Adding a new key-value pair
district_status["Palm Springs"] = "Low"

print(f"Updated dictionary: {district_status}")
