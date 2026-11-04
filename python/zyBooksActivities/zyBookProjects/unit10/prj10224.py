balance = 1000
year = 1
interest = 0.05
while year <= 3:
    print(balance, year)
    year += 1
    intbalance = balance * 0.05
    balance = balance + intbalance

