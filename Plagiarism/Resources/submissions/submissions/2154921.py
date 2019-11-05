def is_even(x):
    if x % 2 == 0:
        return True
    return False

x = int(input("x= "))

result = is_even(x)
print(result)