def modulo_rep_sub(a, b):
    # a % b by doing repeated subtratction
    result = a
    while result - b >= 0:
        result -= b
    return result

def modulo_eq(a, b):
    # a % b by mathematical equation
    return a - (a/b) * b

# For both negative and postive x
# n >= 0
# x % (2 ** n) == x & (2**n - 1)

# (a + b) % n == ((a%n) + (b%n)) % n
# (a - b) % n == ((a%n) - (b%n)) % n
# (a * b) % n == ((a%n) * (b%n)) % n
# (a % n) % n == a % n

# http://www.geeksforgeeks.org/modular-division/
# (a / b) % n is a special case
#   == ((a%n) * ((b ** -1) % n)) % n, when RHS is defined
#   RHS is defined iff b and n are relatively prime

# http://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
# (a ** b) % n too
