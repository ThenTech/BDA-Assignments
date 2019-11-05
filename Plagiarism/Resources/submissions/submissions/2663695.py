s = input("Give a string: ")

mirror = ""
for i in range(0, len(s)):
    mirror = s[i] + mirror

print(mirror)
