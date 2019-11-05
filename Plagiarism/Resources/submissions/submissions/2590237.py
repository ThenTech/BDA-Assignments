def lucky_numbers(n):
    s = [k for k in range(1, n+1)]
    new_s = []
    i = 2
    while i < len(s) + 1:
        new_s = []
        for k in range(len(s)):
            if (k+1) % i != 0:
                new_s.append(s[k])
        s = new_s
        i += 1
    return s
            