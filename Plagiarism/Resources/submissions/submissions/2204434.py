def count_words(s):
    arr = s.split()
    count = 0
    for i in arr:
        isstring = True
        for j in i:
            if not ("A" <= i <= "Z" or "a" <= i <= "z"):
                isstring = False
        if isstring:
            count += 1
    return count