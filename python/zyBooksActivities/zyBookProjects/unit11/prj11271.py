# Write a program that displays the dimensions of a letter-size (8.5 × 11 inch) 
# sheet of paper in millimeters. There are 25.4 millimeters per inch. 
# Use constants and comments in your program.

# Letter width in MM = width of letter * number of MM per 1 inch
# millimeter width = 8.5 inches * 25.4
#
# Letter length in MM = length of letter * number of MM per 1 inch
# millimeter length = 11 inches * 25.4




millimeters = 25.4 # number of millimeters per 1 inch
letterWidth = 8.5 # in inches
letterLength = 11 # in inches

# calculate the width in millimeters
letterWidthMM = 25.4 * 8.5

# calculate the length in millimeters
letterLengthMM = 25.4 * 11

# output the results

print(f"The dimensions of a letter size of paper is ({letterWidthMM:.2f} * {letterLengthMM:.2f} MM)")

