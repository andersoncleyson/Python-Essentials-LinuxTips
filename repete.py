#!/usr/bin/env python3

# numbers = [1, 2, 3, 4, 5, 6]
numbers = range(1, 11) # start, next, stop
# Iterable
for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        continue