x = "abcdefghijklmnopqrstuvwxyz"
y = "abcdefghijklmnopqrstuvwxyz"
q = str(input("Give a sentence: "))
z = str(input("Give a sentence: "))

for i in range(0,26):

    a = q.count(str(x[i]))
    b = z.count(str(y[i]))
    if a != b:
        print(q, "and", z, "are not anagrams")
        break
if a == b:
    print(q, "and", z, "are anagrams")
