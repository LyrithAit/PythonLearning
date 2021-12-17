#!/usr/bin/env python3
def get_number():
    "Returns a float number"
    number = float(input("Enter a float number: "))
    return number

while True:
    try:
        print(get_number())
    except ValueError:
        print("You entered a wrong value.")
