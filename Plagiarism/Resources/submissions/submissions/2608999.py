def lucky_numbers(n):
    n = [x for x in range(1,n+1)]
    if len(n) % 2 == 0:
        el = 1
    else:
        el = 2
    while el <= len(n):
        for x in range(-el, -(len(n))+1):
            del n[x]
        el = el + 1
        
    return n