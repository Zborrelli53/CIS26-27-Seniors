# Variables, Arithmatic, and importing modules

# Demo 1 - Variables and Assignment
def demo1_variables():
    CAN_VOLUME = 0.355 # IN LITERS
    BOTTLE_VOLUME = 2.0 # IN LITERS

    cansPerPack = 6
    packVolume = cansPerPack * CAN_VOLUME
    print("Six-pack volume:", packVolume, "liters")
    print("Two-liter bottle:", BOTTLE_VOLUME, "liters")

demo1_variables()

redTeam = 12
blueTeam = 30

# The scorekeeper switched the scores!
# Make redTeam hp;d 30 and the blueTeam hold 12.
# Rule: do NOT type 12 or 30 again

temp = redTeam
redTeam = blueTeam
blueTeam = temp

print("Red:", redTeam, "Blue:", blueTeam)

# ---------------------------------------------
# Demo 2 - Assignment and Reassignment (11.1)
# ---------------------------------------------

# = means "is set to" or "gets"
lives = 3
print("Lives at start:", lives)
lives = lives + 2     # adding 2 lives to your total
print("After a power-up: ", lives)

# --------------------------------------
# Demo 3 Operators and Precedence (11.2)
# --------------------------------------

print("\n\nOperators and Precedence:")
def demo3_operators():
    a = 10
    b = 4
    print(f"a + b / 2 =", a + b / 2) # 12.0 (Division First)
    print(f"(a + b) / 2 =", (a + b) / 2) # 7.0 
    print(f"10 - 2 - 3 =", 10 - 2 - 3) # 5
    print(f"7 + 4.0 =", 7 + 4.0) # 11.0

    # Powers
    print(f"10 * 2 ** 3", 10 * 2 ** 3) # 80 (** before multiplication)
    print(f"2 ** 3 ** 2 =", 2 ** 3 ** 2) # 512


    # Compound interest: balance * 1 (1 + rate/100) ** years
    balance = 1000.0
    rate = 5.0
    year = 10
    future = balance * (1 + rate / 100) ** 10
    print(f"Future value: {future:.6}")


demo3_operators()

# --------------------------------------
# Demo 4: Floor Division and Modulus
# --------------------------------------

print(f"\n\nFloor Division & Modulus")

def demo4_floor_and_mod():
    print(f"17 / 5 = {17 / 5}") # 3.4
    print(f"17 // 5 = {17 // 5}") # 3
    print(f"17 % 5 = {17 % 5}") # 2

demo4_floor_and_mod()

screenMinutes = 437
time = 60

#Use // and & to store hours and mins,
# then print: 7 hours and 17 minutes

screenHours = (screenMinutes // time)
screenSeconds = screenMinutes % time

print(f"{screenHours} hours and {screenSeconds} minutes")

# -------------------------------------
# Built-in functions return values
# -------------------------------------

print(f"\n\nBuilt-in Functions return values")

print(f"abs(-42) -> {abs(-42)}")
print(f"round(3.14159) -> {round(3.14159)}")
print(f"round(3.14159, 2) -> {round(3.14159, 2)}")
print(f"max(88, 95, 72) -> {max(88, 95, 77)}")
print(f"min(4.99, 3.49) -> {min(4.99, 3.49)}")



# -------------------------------------
# The math Module: import first
# -------------------------------------

print("Three ways to import from a module:")

print("from math import sqrt, cos")
print("sqrt(81)")

print("import math")
print("math.sqrt(81)")

print("from math import *")
print("sqrt(81)")

from math import *

radius = sqrt(50)
print(round(pi * radius ** 2, 2))