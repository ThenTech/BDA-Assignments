a = input()
b = input()
m = "are anagrams"

counter = 0
for i in a:
    for j in b:
        if i == j:
            counter += 1

    if counter == 0:
        m = "are not anagrams"
        break

    counter = 0

print(a, "and", b, m)