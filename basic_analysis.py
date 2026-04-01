"""
Aqua-Alert: Basic Water Quality Analysis Script
-----------------------------------------------
This script performs a simple analysis on water sensor data.
It calculates basic metrics like the average and maximum recorded pH levels.
"""

# Sample data: water pH levels from various sensors
# In a real-world scenario, this data could be loaded from a CSV file.
water_readings = [7.2, 6.8, 7.5, 7.1, 6.9, 8.1, 7.3, 7.0, 7.4, 6.7]

def calculate_average(readings):
    """Calculates the average of a list of readings."""
    if not readings:
        return 0
    return sum(readings) / len(readings)

def analyze_sensor_data(readings):
    """Analyzes sensor readings and prints the summary."""
    print("--- Aqua-Alert: Data Analysis Summary ---")
    print(f"Total readings processed: {len(readings)}")
    
    avg_ph = calculate_average(readings)
    max_ph = max(readings)
    min_ph = min(readings)
    
    print(f"Average pH Level: {avg_ph:.2f}")
    print(f"Maximum pH Level: {max_ph:.2f}")
    print(f"Minimum pH Level: {min_ph:.2f}")
    
    # Simple logic to check if water is within safe pH range (6.5 - 8.5)
    if 6.5 <= avg_ph <= 8.5:
        print("Status: SAFE - Average pH is within the acceptable range.")
    else:
        print("Status: WARNING - Average pH is outside the safe range!")
    
    print("-----------------------------------------")

if __name__ == "__main__":
    # This is the entry point of our script.
    # It executes when the file is run directly.
    analyze_sensor_data(water_readings)
