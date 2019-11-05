def lucky_numbers(n):
    for x in n:
        if x % x ==0:
            n.remove(x)
            