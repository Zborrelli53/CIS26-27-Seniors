# Write a program that computes and displays the perimeter of a letter-size (8.5 × 11 inch) 
# sheet of paper and the length of its diagonal.

# sheet of paper perimiter = (letter width * 2) + (letter length * 2)
# 
# diagonal of a square paper forms a right triangle. So to find the length of the diagonal
# we need to calculate the hypotenuese
# hypoteneuse theory: a ** 2 + b ** 2 = c ** 2

from math import sqrt


letterWidth = 8.5 # in inches
letterLength = 11 # in inches

# Perimeter equation: P = 2L + 2W
perimeter = (2 * letterLength) + (2 * letterWidth)

diagonal = sqrt((letterLength ** 2) + (letterWidth ** 2))

print(f"The perimeter of a letter size paper is {perimeter}")

print(f"The length of the diagonal of a letter size of paper is {diagonal:.2f} inches")