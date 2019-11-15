# ------------------------
# Robot Framework tests
# Some basic things to test the Robot framework
# ------------------------

# ------------------------
# Imports
# ------------------------
import math


def get_sum(*args):
    sum = 0
    for value in args:
        print("MEH")
        print(value)
        sum += value
    return sum


def get_product(num1, num2):
    return num1 * num2


def get_sqrt(num1):
    return math.sqrt(num1)

