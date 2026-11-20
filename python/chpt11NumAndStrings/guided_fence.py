##
#  GUIDED PROJECT: Fence Planner   (Sections 11.3 - 11.7)
#  Your name: ______________________
#
#  STEP 1 - UNDERSTAND THE PROBLEM
#    A fence has a post at BOTH ends. Posts may be no farther apart than
#    a maximum spacing. Each section between two posts needs 2 rails.
#    Posts cost $12.50, rails cost $9.00, and there is 8% sales tax.
#
#  STEP 2 - DO IT BY HAND  (fence 50 ft, max spacing 8 ft)
#    50 / 8 = 6.25 sections  -> round 7 -> 7  sections
#    Posts = sections + 1        = 8
#    Actual spacing = 50 / 7 = 7.14 ft
#    Posts cost:      8 * 12.50  = $100
#    Rails cost:   7 * 2 * $9.00 = $126
#    Subtotal:                     $226
#    Tax:          226.00 * 0.08 = $18.08
#    Total:                        $244.08
#
#  STEP 3 - ALGORITHM  (write it in plain English)
#    sections = round UP(fence length / max spacing)
#    posts    = sections + 1
#    spacing  = Fence length / sections
#    cost     = (Rails Cost + Posts Cost) + Tax = Total
#

# STEP 4 - IMPORTS: import ONLY the function you need from math
from math import ceil


# Constants
POST_PRICE = 12.50
RAIL_PRICE = 9.00
RAILS_PER_SECTION = 2
TAX_RATE = 0.08

# STEP 5 - INPUT: read the fence length and max spacing as floats
fenceLength = float(input("Length of the fence in feet"))
maxSpacing = float(input("Max spacing distance in feet"))


# STEP 6 - COMPUTE: sections, posts, actual spacing
numSections = ceil(fenceLength / maxSpacing)
numPosts = numSections + 1
actualSpacing = fenceLength / numSections


#   Build totalCost as a running total using += (posts, then rails),
#   then apply tax with a single *= statement
totalCost = 0.0
totalCost += numPosts * POST_PRICE
totalCost += numSections * RAILS_PER_SECTION * RAIL_PRICE
totalCost *= 1 + TAX_RATE


# STEP 7 - OUTPUT: print sections, posts, spacing, and total cost.
#   Split at least one long print statement across two lines
#   (inside the parentheses!)

print(f"Sections needed {numSections}")
print(f"Posts needed: {numPosts}")
print("Posts will be",
      round(actualSpacing, 2))
print("Total cost with tax: $",
      round(totalCost, 2))



# STEP 8 - TEST: run with 50 and 8. Does it match your hand calculation?
#   Then try 48 and 8. Predict the answer first!
