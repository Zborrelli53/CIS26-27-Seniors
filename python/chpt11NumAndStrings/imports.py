# ----------------------------------------------------------------------
# Section 11.3 Practice: Other ways to import modules
# Demonstrates the different ways to bring math functions into a program
# ----------------------------------------------------------------------

# -------------------------------------------
# Style 1: Import specific funcitons by name
# -------------------------------------------

from math import sqrt, ceil, floor

print(f"Style 1: from math import sqrt, ceil, floor")
print(f"sqrt(81) = {sqrt(81)}")
print(f"ceil(4.2) = {ceil(4.2)}")
print(f"floor(4.8) = {floor(4.8)}")

# ----------------------------------------------------------
# Style 2: Import the whole module, then use module.function
# ----------------------------------------------------------

import math

print(f"\nStyle 2: import math")
print(f"math.sqrt(81) = {math.sqrt(81)}")
print(f"math.pi = {math.pi}")
print(f"math.pow(2, 5) = {math.pow(2, 5)}")

# ------------------------------------------------------------------
# Style 3: Import everything with the * (Works but use with caution)
# ------------------------------------------------------------------

from math import *
print(f"\nStyle 3: from math import *")
print(f"cos(0) = {cos(0)}")
print(f"e = {e}")
e = 5
print(f"e = {e}")


