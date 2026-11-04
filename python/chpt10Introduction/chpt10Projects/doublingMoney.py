# ================================================
# Script Name: doublingMoney.py
# Lesson: Algorithm Design (Section 10.9)
#
# Problem (from the textbook)
#   You put $10,000 into an account that earns 5% interest
#   per year. How many years until the balance doubles
#
# Pseudocode (my algorithm): 
#   Set year to 0, balance to 10000
#   While the balance less than 20,000
#       Add 1 to the year
#       Set the interest to balance X 0.05
#       Add the interest to the balance.
#   Report year as the answer

#   Set year to 0, balance to 10000
year = 0
balance = 10000

# While the balance less than 20,000
while balance < 20000:
    # add 1 to the year
    # year = year + 1
    year += 1
    # set the interest to balance x 0.05
    interest = balance * 0.05
    # Add the interest to the balance
    balance = balance + interest

# report year as the answer
print("Years to double: ", year)
print("Final balance: ", "$", f"{balance:.2f}")
