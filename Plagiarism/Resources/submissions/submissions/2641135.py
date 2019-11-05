def lucky_numbers(n):
    s = [i for i in range(1, n + 1)]
    pass = 2
    while pass <= len(s):
        s = [s[i] for i in range(0,len(s)) if (i + 1) % pass != 0]
        pass += 1
    return s