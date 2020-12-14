#/usr/bin/env python3
from fractions import Fraction # Helps with contined fractions
import math

e = 42667
n = 64741

# Returns whether true or false for whether the solutions to quadratic are integers
def check_quadratic(phi, n):
    a = 1
    b = -(n - phi + 1)
    c = n

    determinant = b**2 - 4*a*c

    # No imaginary solutions allowed
    if determinant < 0:
        return False
    
    root = math.isqrt(determinant)

    # If determinant is not perfect square then that means the roots are not integers
    if root ** 2 != determinant:
        return False
    
    # Check to make sure roots are integers
    if (-b + root) % (2*a) != 0 or (-b - root) % (2*a) != 0:
        return False

    q = (-b + root) // (2*a)
    p = (-b - root) // (2*a)

    print("q: " + str(q))
    print("p: " + str(p))

    # If nothing else return False then the solutions are integers
    return True

# Returns whether totient is whole number or not
def totient_whole_number(d, k, e):
    if k == 0:
        return False
    return (d * e - 1) % k == 0

# Performs the three checks to make sure we have the right value for d and k
def perform_check(d, k):
    if d == 1:
        return False

    # First check: Check for odd parity
    if d % 2 == 0:
        return False
    # Second check: Check to make sure totient is whole number
    if not totient_whole_number(d, k, e):
        return False

    # If we pass 2nd test then calculate the possible phi value
    phi = (d * e - 1) // k

    # Third check: Check for integer solution to quadratic
    if not check_quadratic(phi, n):
        return False

    return True

# Converts the sequence to a convergent which might be a possibility for k/d
def sequence_to_d_and_k(sequence):
    # If only one element in sequence
    if len(sequence) == 1:
        return 1, sequence[0]

    convergent = 0

    # Traverse sequence in reverse order
    for elem in sequence[::-1]:
        if (convergent == 0):
            convergent = elem
        else:
            convergent = elem + Fraction(1, convergent)

    k = convergent.numerator
    d = convergent.denominator

    return d, k

def continued_fraction(e, n):
    # Stores the sequence from euclid's algorithm
    sequence = []

    a = e
    b = n

    # Use euclid's algorithm to get the convergents/continued fraction
    while (a != 0 and b != 0):
        quotient = a // b
        r = a % b
        a = b
        b = r

        sequence.append(quotient)

        # Converts the sequence to the convergent
        d, k = sequence_to_d_and_k(sequence)

        # print(d, k)

        # If all the checks are passed, there's no need to continue since we've found d
        if (perform_check(d, k)):
           return d

    # print(sequence)

d = continued_fraction(e, n)

print("Your value for d is " + str(d))
