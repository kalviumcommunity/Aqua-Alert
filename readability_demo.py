# ---------------------------------------------------------
# Aqua-Alert: Code Readability and Intent Demonstration
# ---------------------------------------------------------

def calculate_average_rainfall(daily_rainfall_amounts):
    """
    Calculates the average rainfall over a provided sequence of days.
    """
    # Calculate total and determine the number of days recorded
    total_rainfall_mm = sum(daily_rainfall_amounts)
    number_of_days = len(daily_rainfall_amounts)
    
    # Prevent division by zero if the dataset is empty
    if number_of_days == 0:
        return 0.0
        
    average_rainfall_mm = total_rainfall_mm / number_of_days
    
    return average_rainfall_mm


def evaluate_flood_risk(average_rainfall_mm, flood_threshold_mm):
    """
    Evaluates whether the given average rainfall exceeds the safety threshold.
    """
    # Return a boolean indicating if the threshold was crossed
    is_risk_high = average_rainfall_mm >= flood_threshold_mm
    return is_risk_high


if __name__ == '__main__':
    # Simulated daily rainfall data in millimeters over a 5-day period
    recent_rainfall_data = [12.5, 8.0, 0.0, 22.1, 5.4]
    
    # The critical threshold at which flood warnings are triggered
    flood_warning_threshold_mm = 15.0
    
    # Use descriptive variable names to capture returned values
    average_recent_rainfall = calculate_average_rainfall(recent_rainfall_data)
    flood_risk_detected = evaluate_flood_risk(average_recent_rainfall, flood_warning_threshold_mm)
    
    print("--- Aqua-Alert: Flood Risk Evaluation ---")
    print(f"Average Rainfall: {average_recent_rainfall:.2f} mm")
    print(f"Warning Threshold: {flood_warning_threshold_mm} mm")
    
    if flood_risk_detected:
        print("ALERT: High flood risk detected due to excessive average rainfall!")
    else:
        print("INFO: Rainfall is within normal, safe limits.")
