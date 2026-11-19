##
# Section 11.5 Practice: Line joining
# Splitting long statements across multiple lines.
#
#

from math import sqrt

a = 1
b = -3
c = 2

# --- Implicit joining: Break the line INSIDE parentheses ---
x1 = ((-b + sqrt(b ** 2-4 * a * c))
      / (2 * a))
print(f"x1 (Parentheses) = {x1}")

# -- Explicit Joining: end the line with a backslash ---
# works, but NOTHING may follow the \ -- not even a space
x2 = (-b - sqrt(b ** 2 - 4 * a * c)) \
    / (2 * a)
print(f"x2 (Backslash) = {x2}")