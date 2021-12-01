#!/usr/bin/env python3
amount = float(input("Enter amount: ")) #Enter Amount
inrate = float(input("Enter Interest rate: ")) #Enter Rate
period = int(input("Enter period: ")) #Enter Period
value = 0
year = 1

while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year, value))
    amount = value
    year = year + 1
    