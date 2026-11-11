# Temperature Monitor and Alarm Checker
# Author: BALOGUN YUSUF OLAITAN
#
# The user enters 5 temperature readings from a machine in degrees Celsius.
# The program stores them in a list, prints the highest, lowest and average,
# and warns if any reading is above the safe limit.
#
# My own twist: every reading gets a status label.
#   Normal             - well below the safe limit
#   Warning            - within 5 C of the limit, so the machine is getting close
#   ALARM              - above the safe limit
# The program also counts how many readings were in each group.

SAFE_LIMIT = 80.0          # highest safe temperature in degrees Celsius
WARNING_MARGIN = 5.0       # readings this close to the limit get a warning
NUMBER_OF_READINGS = 5     # how many readings the user enters each time
ABSOLUTE_ZERO = -273.15    # the lowest temperature possible, in degrees Celsius


def ask_temperature(number):
    """Ask for one reading and keep asking until it is a valid temperature."""
    while True:
        text = input(f"Enter reading {number} in C: ").strip()

        # Check that the input is a number at all
        try:
            value = float(text)
        except ValueError:
            print("  That is not a number. Try again, for example 72.5.")
            continue

        # Check that the temperature is physically possible
        if value < ABSOLUTE_ZERO:
            print("  That is below absolute zero (-273.15 C), so it cannot be right. Try again.")
            continue

        return value


def get_readings():
    """Collect all the readings into a list."""
    readings = []
    for number in range(1, NUMBER_OF_READINGS + 1):
        readings.append(ask_temperature(number))
    return readings


def status_of(temperature):
    """Return the status label for one reading (the twist)."""
    if temperature > SAFE_LIMIT:
        return "ALARM: above safe limit"
    elif temperature >= SAFE_LIMIT - WARNING_MARGIN:
        return "Warning: close to limit"
    else:
        return "Normal"


def report(readings):
    """Print each reading with its status, then the summary."""
    print("\n--- Readings ---")
    for number, temperature in enumerate(readings, start=1):
        print(f"  Reading {number}: {temperature:.1f} C  ->  {status_of(temperature)}")

    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    print("\n--- Summary ---")
    print(f"  Highest: {highest:.1f} C")
    print(f"  Lowest:  {lowest:.1f} C")
    print(f"  Average: {average:.1f} C")

    # Count how many readings fell into each group
    alarms = sum(1 for t in readings if t > SAFE_LIMIT)
    warnings = sum(1 for t in readings if SAFE_LIMIT - WARNING_MARGIN <= t <= SAFE_LIMIT)
    normal = len(readings) - alarms - warnings
    print(f"  Normal: {normal}   Warning: {warnings}   Alarm: {alarms}")

    if alarms > 0:
        print(f"\n  ALARM: {alarms} reading(s) are above the safe limit of {SAFE_LIMIT:.0f} C.")
    else:
        print("\n  All readings are within the safe limit.")


def main():
    print("=== Temperature Monitor and Alarm Checker ===")
    print(f"Safe limit: {SAFE_LIMIT:.0f} C. Enter {NUMBER_OF_READINGS} readings.")

    # Loop so the user can check another set of readings without restarting
    while True:
        readings = get_readings()
        report(readings)

        again = input("\nCheck another set of readings? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped. Goodbye.")
