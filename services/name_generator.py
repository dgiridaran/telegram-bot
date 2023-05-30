import string
import random


def generate_new_name(N: int):
    new_name = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
    return new_name

