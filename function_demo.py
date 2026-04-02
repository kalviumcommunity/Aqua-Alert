# ---------------------------------------------------------
# Aqua-Alert: Function Data Flow Demonstration
# ---------------------------------------------------------

def calculate_water_level_change(initial_level, final_level):
    """
    Calculates the change in water level.
    
    Parameters:
    initial_level (float): The starting water level in meters.
    final_level (float): The ending water level in meters.
    
    Returns:
    float: The difference between final_level and initial_level.
    """
    # 2. Use of parameters inside the function logic
    level_change = final_level - initial_level
    
    # 3. Returning a value using return
    return round(level_change, 2)

def generate_alert_message(location, level_change):
    """
    Generates an alert message based on the water level change.
    
    Parameters:
    location (str): Name of the monitored district.
    level_change (float): The change in water level.
    
    Returns:
    str: The generated alert message.
    """
    if level_change > 0:
        return f"ALERT: Water level at {location} has increased by {level_change} meters."
    elif level_change < 0:
        return f"INFO: Water level at {location} has decreased by {abs(level_change)} meters."
    else:
        return f"INFO: Water level at {location} remains stable."

# ---------------------------------------------------------
# Execution / Demonstration
# ---------------------------------------------------------

if __name__ == "__main__":
    print("--- Aqua-Alert: Function Data Flow Demo ---\n")

    # Define some input data
    district_name = "Riverside"
    morning_water_level = 15.5
    evening_water_level = 16.8

    print(f"Location: {district_name}")
    print(f"Morning Level: {morning_water_level}m")
    print(f"Evening Level: {evening_water_level}m")

    # 1. & 4. Pass arguments into the function and store returned value
    change_result = calculate_water_level_change(morning_water_level, evening_water_level)
    print(f"\nCalculated Change: {change_result}m")

    # 5. Reusing the returned value meaningfully
    # Passing the returned 'change_result' as an argument to another function
    alert_output = generate_alert_message(district_name, change_result)
    
    print("\nGenerated System Message:")
    print(alert_output)
