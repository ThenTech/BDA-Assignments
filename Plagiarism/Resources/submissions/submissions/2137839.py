number = input('number?')
i = len(number)-1
q = 0
while i >= 0:
    if (int(number[i])) % 2 == 0:
        q+=1
    i -= 1
print(q)
