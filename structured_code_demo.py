"""
User Profile Formatter

This script demonstrates structuring Python code for readability and reuse.
It processes raw user data, formats it consistently, and displays the results.
"""

# ==============================================================================
# SECTION 1: IMPORTS
# ==============================================================================
import datetime

# ==============================================================================
# SECTION 2: REUSABLE FUNCTIONS (LOGIC & PROCESSING)
# ==============================================================================

def format_name(first_name, last_name):
    """
    Capitalizes the first letter of both first and last names.
    Returns the formatted full name.
    """
    formatted_first = first_name.strip().capitalize()
    formatted_last = last_name.strip().capitalize()
    return f"{formatted_first} {formatted_last}"

def calculate_age(birth_year):
    """
    Calculates the current age based on the birth year.
    Returns an integer age.
    """
    current_year = datetime.date.today().year
    return current_year - birth_year

def generate_profile_summary(first_name, last_name, birth_year, occupation):
    """
    Uses helper functions to generate a complete profile summary string.
    """
    full_name = format_name(first_name, last_name)
    age = calculate_age(birth_year)
    
    return f"Profile: {full_name} is {age} years old and works as a {occupation}."

# ==============================================================================
# SECTION 3: EXECUTION LOGIC (MAIN FLOW)
# ==============================================================================

def main():
    """
    Main execution function. Separates logic from execution so this script
    can be imported safely into other files if needed.
    """
    print("--- Starting User Data Processing ---\n")

    # Sample raw data (simulating input from a database or file)
    user_1 = {"first": " alice ", "last": "smith", "birth_year": 1995, "job": "Software Engineer"}
    user_2 = {"first": "BOB", "last": " jones ", "birth_year": 1988, "job": "Data Analyst"}
    user_3 = {"first": " charlie", "last": "BROWN ", "birth_year": 2001, "job": "Product Manager"}

    # Process and display each user using the reusable functions
    print(generate_profile_summary(user_1["first"], user_1["last"], user_1["birth_year"], user_1["job"]))
    print(generate_profile_summary(user_2["first"], user_2["last"], user_2["birth_year"], user_2["job"]))
    print(generate_profile_summary(user_3["first"], user_3["last"], user_3["birth_year"], user_3["job"]))

    print("\n--- Processing Complete ---")

# Evaluate and execute only when run directly
if __name__ == "__main__":
    main()
