"""
Traffic Light Control Program.

This program takes traffic light color as input
and displays the corresponding action.
"""

light = input("light color: ")

if light == "red":
    print("stop")
elif light == "yellow":
    print("look")
elif light == "green":
    print("go")
else:
    print("not valid")
