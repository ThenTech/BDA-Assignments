x = int(input("Number?"))
x == True

def is_even(x):
    if x % 2 != 1:
        x = True
        return x
    else:
        x = False
        return x


print(is_even(x))