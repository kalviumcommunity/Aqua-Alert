# ---------------------------------------------------------
# Aqua-Alert: Data Types Demonstration
# ---------------------------------------------------------

# 1. Integer and Floating-Point Variables
target_districts = 5                # Integer
average_rainfall_mm = 120.5         # Float

print("--- Numeric Types ---")
print(f"Tracking {target_districts} districts. (Type: {type(target_districts).__name__})")
print(f"Average rainfall recorded: {average_rainfall_mm} mm. (Type: {type(average_rainfall_mm).__name__})\n")


# 2. String Variables with Meaningful Values
region_name = "Riverside County"
warning_status = "Critical"

print("--- String Types ---")
print(f"Region: {region_name} (Type: {type(region_name).__name__})")
print(f"Status: {warning_status} (Type: {type(warning_status).__name__})\n")


# 3. Arithmetic Operations on Numeric Types
days_of_rain = 3 # Integer
total_expected_rainfall = average_rainfall_mm * days_of_rain

print("--- Arithmetic Operations ---")
print(f"If it rains for {days_of_rain} days at the average rate, "
      f"expected rainfall = {total_expected_rainfall} mm\n")


# 4. String Concatenation and Formatting
print("--- String Manipulation ---")
# Using Concatenation (+)
concat_message = "WARNING: " + region_name + " is currently at a '" + warning_status + "' alert level!"
print("Concatenated:", concat_message)

# Using F-string formatting
formatted_message = f"UPDATE: {region_name} expects {total_expected_rainfall} mm of rain."
print("Formatted:   ", formatted_message, "\n")


# 5. Type Mismatch and Conversion Example
print("--- Type Conversion & Mismatch ---")
# Simulating a sensor reading that comes in as text (string)
sensor_reading_str = "45.5"

print("Attempting to add a Float and a String without conversion...")
try:
    # This will trigger a TypeError
    faulty_addition = average_rainfall_mm + sensor_reading_str
except TypeError as error:
    print(f"-> Caught an Error: {error}")

# Now we properly convert (cast) the string to a float
print("\nConverting the 'sensor_reading_str' to a Float...")
sensor_reading_converted = float(sensor_reading_str)
correct_addition = average_rainfall_mm + sensor_reading_converted

print(f"Success! {average_rainfall_mm} + {sensor_reading_converted} = {correct_addition}")
