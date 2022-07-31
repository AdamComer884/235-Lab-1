import random
from numberChecker import check_is_even, check_is_prime, generate_array
from game import UPPER_VAL, LOWER_VAL
import enum


class SelectionSet(enum.Enum):
    Numbers: tuple = tuple([i for i in range(LOWER_VAL, UPPER_VAL)])
    Even: tuple = generate_array(check_is_even)
    Prime: tuple = generate_array(check_is_prime)


def pick_a_number(option: list or tuple) -> int:
    return random.choice(option)
