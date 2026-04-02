"""
Aqua-Alert: Conditional Logic Demo
This script demonstrates the use of if, elif, else statements and logical operators.
"""

def main():
    # --- Part 1: Basic 'if' Condition (Numeric comparison) ---
    water_level = 85  # Current water level in percentage
    print(f"Current Water Level: {water_level}%")
    
    if water_level > 80:
        print("ALERT: Water level is CRITICAL! Prepare for drainage.")

    # --- Part 2: 'if-else' Branching Logic (String comparison) ---
    sensor_status = "active"
    print(f"\nSensor Status: {sensor_status}")
    
    if sensor_status == "active":
        print("Decision: System is monitoring in real-time.")
    else:
        print("Decision: System is offline. Manual check required.")

    # --- Part 3: 'if-elif-else' Structure (Multiple numeric conditions) ---
    rainfall_rate = 15  # Rainfall rate in mm/hour
    print(f"\nCurrent Rainfall Rate: {rainfall_rate} mm/hour")
    
    if rainfall_rate > 30:
        print("Condition: Extreme Rainfall. Flooding highly likely.")
    elif rainfall_rate > 10:
        print("Condition: Heavy Rainfall. Monitor drainage channels.")
    elif rainfall_rate > 2:
        print("Condition: Moderate Rain. No immediate action needed.")
    else:
        print("Condition: Light Rain or No Rain. Safe conditions.")

    # --- Part 4: Logical Operators (and, or, not) ---
    high_humidity = True
    strong_winds = False
    
    print(f"\nWeather Check - High Humidity: {high_humidity}, Strong Winds: {strong_winds}")
    
    # Using 'and' and 'or'
    if high_humidity and rainfall_rate > 10:
        print("Analysis: High probability of persistent heavy rain.")
        
    if rainfall_rate > 20 or strong_winds:
        print("Analysis: Structural stability caution recommended.")
    
    # Using 'not'
    system_maintenance_mode = False
    if not system_maintenance_mode:
        print("System: Automated alert protocols are enabled.")

    print("\n--- Conditional Logic Demonstration Finished ---")

if __name__ == "__main__":
    main()
