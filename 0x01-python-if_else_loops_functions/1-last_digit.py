#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_digit_signed = -last_digit if number < 0 else last_digit

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit_signed} \
            and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit_signed} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit_signed} \
        and is less than 6 and not 0")
