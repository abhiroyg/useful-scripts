def is_odd(a):
    # Correct only for numbers >= 0
    return a % 2 == 1

def is_odd(a):
    # Negative odd numbers give -1 as remainder
    # though negative even numbers give 0
    return a % 2 != 0
    return a % 2 == 1 or a % 2 == -1

