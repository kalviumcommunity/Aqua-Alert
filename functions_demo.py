"""
Aqua-Alert: Functions Milestone Demo
This script demonstrates defining functions, calling them,
passing arguments, and understanding basic scope.
"""

# Global variable used only for scope demonstration
alert_region = "Riverside"


def print_header(title):
    """Print a formatted section header."""
    print(f"\n--- {title} ---")


def calculate_risk_score(rainfall_mm, water_level_percent):
    """Return a simple risk score from two numeric inputs."""
    return rainfall_mm * 0.4 + water_level_percent * 0.6


def classify_risk(score):
    """Classify numeric risk score into a text label."""
    if score >= 80:
        return "Critical"
    if score >= 50:
        return "Moderate"
    return "Low"


def show_alert_message(region, severity):
    """Function with parameters that prints a reusable message."""
    print(f"Alert for {region}: {severity} risk level")


def scope_demo():
    """Demonstrate local and global variable behavior."""
    print_header("Part 4: Function Scope")
    local_status = "Local monitoring active"

    print(f"Inside function - global variable alert_region: {alert_region}")
    print(f"Inside function - local variable local_status: {local_status}")


def main():
    print("Aqua-Alert Functions Milestone")

    print_header("Part 1: Defining and Calling Functions")
    print("Function print_header() has been defined and called.")

    print_header("Part 2: Parameters and Arguments")
    rainfall_today = 62
    water_level_today = 74
    print(f"Inputs -> rainfall={rainfall_today}, water_level={water_level_today}")

    risk_score = calculate_risk_score(rainfall_today, water_level_today)
    severity = classify_risk(risk_score)

    print(f"Computed risk score: {risk_score:.1f}")
    show_alert_message(alert_region, severity)

    print_header("Part 3: Execution Flow")
    print("Flow: main() -> calculate_risk_score() -> classify_risk() -> show_alert_message()")
    print("Control returns to main() after each function finishes.")

    scope_demo()

    print("\nOutside function - global variable alert_region is still available:")
    print(f"alert_region = {alert_region}")
    print("local_status is not available here because it is local to scope_demo().")

    print("\n--- Functions Demonstration Finished ---")


if __name__ == "__main__":
    main()