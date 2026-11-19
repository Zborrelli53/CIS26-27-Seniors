# Write a program that computes and displays the perimeter of a letter-size (8.5 × 11 inch) 
# sheet of paper and the length of its diagonal.

# sheet of paper perimiter = (letter width * 2) + (letter length * 2)
# 
# diagonal of a square paper forms a right triangle. So to find the length of the diagonal
# we need to calculate the hypotenuese
# hypoteneuse theory: a ** 2 + b ** 2 = c ** 2


letterWidth = 8.5 # in inches
letterLength = 11 # in inches

# Perimeter equation: P = 2L + 2W
perimeter = (2 * letterLength) + (2 * letterWidth)

print(f"The perimeter of a letter size paper is {perimeter}")