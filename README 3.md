# Temperature Monitor and Alarm Checker

## What it does
The user enters 5 temperature readings from a machine in degrees Celsius. The program stores them in a list, prints the highest, lowest and average, and warns if any reading is above the safe limit of 80 C. It rejects text and temperatures below absolute zero, and it can repeat the check with a new set of readings.

## How to run it
Install Python 3, then run: python temperature_monitor.py

## Sample output
```
=== Temperature Monitor and Alarm Checker ===
Safe limit: 80 C. Enter 5 readings.
Enter reading 1 in C: 70
Enter reading 2 in C: 78
Enter reading 3 in C: 82
Enter reading 4 in C: 60
Enter reading 5 in C: -300
  That is below absolute zero (-273.15 C), so it cannot be right. Try again.
Enter reading 5 in C: 76

--- Readings ---
  Reading 1: 70.0 C  ->  Normal
  Reading 2: 78.0 C  ->  Warning: close to limit
  Reading 3: 82.0 C  ->  ALARM: above safe limit
  Reading 4: 60.0 C  ->  Normal
  Reading 5: 76.0 C  ->  Warning: close to limit

--- Summary ---
  Highest: 82.0 C
  Lowest:  60.0 C
  Average: 73.2 C
  Normal: 2   Warning: 2   Alarm: 1

  ALARM: 1 reading(s) are above the safe limit of 80 C.

Check another set of readings? (y/n): n
Goodbye.
```

## My own twist
Every reading gets a status label. Readings above 80 C raise an ALARM, readings within 5 C of the limit are marked as a Warning so the operator can act early, and the rest are Normal. The summary also counts how many readings fall into each group.

## What I learned
Input checks matter in measurement work: the program rejects temperatures below absolute zero, which cannot come from a real sensor. Using a list and the built-in max, min and sum functions made the summary short and easy to check. Putting the limits at the top of the file means they can be changed in one place.

## Author
BALOGUN YUSUF OLAITAN, ND1 Mechatronics Engineering, YabaTech.
