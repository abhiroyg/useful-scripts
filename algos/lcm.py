# python 3
def lcm(a, b):
    # (a * b) % gcd(a, b) is always equal to zero
    # (a * b) / gcd(a, b) gives a float, so use '//'
    return (a * b) // gcd(a, b)
