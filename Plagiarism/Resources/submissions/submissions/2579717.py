def lucky_numbers(n):
    allelist = []
    for i in range(1, n+1):
        allelist.append(i)
    aangepast = delete(allelist)
    return aangepast

def delete(full):
    j = 1
    aangepast = full[:]
    while len(aangepast) >= j:
        j += 1
        aangepast = full[:]
        for i in range(1, len(aangepast[:])+1):
            if i % j == 0:
                full.remove(aangepast[i-1])
            else:
                continue
    return aangepast