##
#  Section 11.7 Worked Example: Computing Travel Time
#  A robot drives along a road (fast), then cuts straight across rocky
#  terrain (slow) to reach an item. Compute the total travel time.
#
#  HAND CALCULATION (distx = 4 road1 = 10 km, disty = 3 km, length1 = 6 km, speed1 = 5 km/h, speed2 = 2 km/h):
#    Segment 1 time   = 6 / 5 = 1.2
#    Segment 2 length = square root((4 ** 2) + (3 ** 2)) = 5
#    Segment 2 time   = 5 / 2 = 2.5
#    Total time       = 1.2 + 2.5 = 3.7
#
from math import sqrt

# Short hand-calculation names (dx, s1...) become DESCRIPTIVE names in code.


# ---------------------------------------------------------------
# TRY IT
#  1. Run with 10, 3, 6, 5, 2.  Does the program match the hand value 3.7?
#  2. By hand: what if the robot drives 8 km on the road instead of 6?
#     (Hint: segment 2 becomes a 2-3 right triangle.) Then check it.
#  3. Rewrite the import as "import math". What else must change?
# ---------------------------------------------------------------

distX = 0
distY = 3
road1 = 10
leng1 = 6
leng2 = 0
speed1 = 5
speed2 = 2

distX = road1 - leng1

time1 = leng1 / speed1
leng2 = sqrt((4 ** 2) + (3 ** 2))
time2 = leng2 / speed2
totalTime = time1 + time2
print(f"The total time for Zander to arrive home is {totalTime} Hours")