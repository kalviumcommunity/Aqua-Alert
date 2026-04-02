"""
Aqua-Alert: Iteration Milestone Demo
This script demonstrates for loops, while loops, break/continue,
and safe patterns to avoid infinite loops.
"""


def for_loop_examples():
    print("--- Part 1: for Loops ---")

    # for loop over a known numeric sequence
    print("Rainfall checks by hour:")
    for hour in range(1, 6):
        print(f"Hour {hour}: sensor check complete")

    # for loop over a collection
    districts = ["Riverside", "Orange County", "San Diego", "Coachella Valley"]
    print("\nDistrict monitoring list:")
    for district in districts:
        print(f"Monitoring district: {district}")


def while_loop_examples():
    print("\n--- Part 2: while Loops ---")

    # condition-based repetition with clear variable updates
    reservoir_level = 78
    target_level = 70
    minute = 1

    print(f"Starting reservoir level: {reservoir_level}%")
    while reservoir_level > target_level:
        print(f"Minute {minute}: level={reservoir_level}% -> drainage active")
        reservoir_level -= 2
        minute += 1

    print(f"Loop stopped safely at {reservoir_level}%. Target reached.")


def loop_control_examples():
    print("\n--- Part 3: break and continue ---")

    # Mixed data to show skipping invalid values and stopping early on critical values
    readings = [12, 15, None, 18, 41, 20]
    critical_threshold = 40

    for reading in readings:
        if reading is None:
            print("Skipping missing reading with continue")
            continue

        if reading >= critical_threshold:
            print(f"Critical value {reading} detected -> break loop")
            break

        print(f"Processed reading: {reading}")


def infinite_loop_safety_examples():
    print("\n--- Part 4: Avoiding Infinite Loops ---")

    # Unsafe pattern (do not execute):
    # while True:
    #     print("This never stops")

    # Safe pattern: condition changes each iteration
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        print(f"Safe retry attempt: {attempts + 1}")
        attempts += 1

    print("Loop ended because the condition became False.")


def main():
    print("Aqua-Alert Iteration Milestone")
    for_loop_examples()
    while_loop_examples()
    loop_control_examples()
    infinite_loop_safety_examples()
    print("\n--- Iteration Demonstration Finished ---")


if __name__ == "__main__":
    main()