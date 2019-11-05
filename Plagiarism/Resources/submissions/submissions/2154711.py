def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


x = int(input("Geef een waarde x in : "))
check = is_even(x)
print(check)