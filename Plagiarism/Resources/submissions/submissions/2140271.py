a = input()
b = input()
m = "are anagrams"
for i in a:
    if i not in b:
        m = "are not anagrams"
        break

print(a, "and", b, m)