#!/usr/bin/env python3
while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue
    elif n == 0:
        break
    print(n, "Square is", n ** 2, "(Enter 0 to exit)")

print("Goodbye")