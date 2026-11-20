##
#  
#  Plans drone delivery trips from a warehouse to a customer and reports
#  the straight-line distance, number of trips, total distance flown,
#  and total time (flying + loading).
#
# Part A - HAND CALCULATION (3 km east, 4 km north, 40 km/h, 7 packages, 2 per trip)
#
#  Import style: "import math" - writing math.sqrt and math.ceil makes it
#  clear to any reader which module each function comes from.

#  distance = square root((3 ** 2) + (4 ** 2))
#  number of trips = ceil(7 / 2)
#  total distance = distance * number of trips
#  total time = total distance / speed

#

import math

eastDist = 3
northDist = 4
speed = 40
numPackages = 7
packagesPerTrip = 2

distance = math.sqrt((eastDist ** 2) + (northDist ** 2))
trips = math.ceil(numPackages / packagesPerTrip)
totalDistance = distance * trips
time = totalDistance / speed

print(f"The total distance traveled is {totalDistance}km, and the total time traveled is {time}")

