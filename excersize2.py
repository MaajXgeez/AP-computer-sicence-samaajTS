import pandas as pd
import nfl_data_py as nfl

# Import 2024 season data
schedules = nfl.import_schedules([2024])
weeklyStats = nfl.import_weekly_data([2024])
pbp = nfl.import_pbp_data([2024])

def sum_numbers(predefined_inputs=None):
    total = 0
    inputs = predefined_inputs or []

    i = 0
    while True:
        try:
            if predefined_inputs:
                if i >= len(predefined_inputs):
                    break
                number_input = inputs[i]
                print(f"Enter a number: {number_input}")
                i += 1
            else:
                number_input = input("Enter a number: ")

            number = float(number_input)
            total += number
        except ValueError:
            print(f"'{number_input}' is not a valid number. Please try again.")
            continue

        if not predefined_inputs:
            done = input("Are you done entering numbers? (yes/no): ").strip().lower()
            if done == "yes":
                break

    print(f"\nThe sum of the numbers you entered is: {total}")
    return total


# To run with simulated inputs (good for non-interactive environments like Codespaces):
sum_numbers(["10", "20.5", "5.5"])
