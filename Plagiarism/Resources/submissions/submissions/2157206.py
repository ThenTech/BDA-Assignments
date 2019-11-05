def is_even(x):
    """Checks if a number x is even and returns True if even or False if uneven"""
    return x % 2 == 0

x = int(input("Give value for x"))

print(is_even(x))
