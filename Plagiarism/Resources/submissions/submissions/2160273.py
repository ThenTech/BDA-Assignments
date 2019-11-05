def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

x = int(input('Zet hier een natuurlijk getal:'))
print(is_even(x))