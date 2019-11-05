w1 = input('First word?')
w2 = input('Second word?')
i = len(w1) - 1
k = len(w2) - 1
q = 0
while i >= 0:
    while k >= 0:
        if w1[i] == w2[k]:
            q += 1
            break
        k -= 1
    i -= 1
    k = len(w2)-1
if q == len(w1):
    print(w1, 'and', w2, 'are anagrams')
else:
    print(w1, 'and', w2, 'are not anagrams')
