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

    #Convert a video length in seconds to minutes and seconds
    videoSeconds = 754
    minutes = videoSeconds // 60
    seconds = videoSeconds % 60
    print(f"Video length: {minutes} min {seconds} sec")

    # Digit Tricks
    n = 2026
    print(f"Last digit {n % 10}") # 6
    print(f"Without last digit: {n // 10}") #202
    print(f"Even? remainder is: {n % 2}") # 0

    

demo4_floor_and_mod()

#Demo 5 - Built-In funcitons, the math module, roundoff (11.2)
print("\n\nDemo 5 - Built-In funcitons, the math module, roundoff (11.2)")

def demo5_functions():
    from math import sqrt, pi

    # Built-in functions: no import needed
    print(f"abs(-42) = {abs(-42)}") # 42
    print(f"round(3.14159) = {round(3.14159)}") # 3
    print(f"round(3.14159, 3) = {round(3.14159, 3)}") # 3.142
    print(f"max(52, 64, 37, 89, 34) = {max(52, 64, 37, 89, 34)}") # 89
    print(f"min(52, 64, 37, 89, 34) = {min(52, 64, 37, 89, 34)}") # 34

    # math module functions: must be imported
    a = 3
    b = 4
    hypotenuse = sqrt(a ** 2 + b ** 2)
    print(f"Hypotenuse: {hypotenuse}")

    print("\n\nFind the area of a circle:")
    radius = 2.5
    area = pi * radius ** 2
    print(f"Circle Area: {round(area, 2)}")

    print("\n\n Roundoff error: binary can't store 4.35 exactly")
    price = 4.35
    quantity = 100
    total = price * quantity
    print(f"Total = {round(total)}")


demo5_functions()



