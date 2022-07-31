from game import LOWER_VAL, UPPER_VAL
import math


def generate_array(function) -> tuple:
    temp = []
    for i in range(LOWER_VAL, UPPER_VAL):
        if function(i):
            temp.append(i)
    return tuple(temp)


def check_is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def check_is_prime(number):
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True
