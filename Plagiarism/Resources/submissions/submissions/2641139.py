def lucky_numbers(n):
    s = [i for i in range(1, n + 1)]
    pas = 2
    while pas <= len(s):
        s = [s[i] for i in range(0,len(s)) if (i + 1) % pas != 0]
        pas += 1
    return s