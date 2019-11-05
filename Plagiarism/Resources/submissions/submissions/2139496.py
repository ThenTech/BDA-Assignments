s = input("Geef een string: ")

tellerBegin = 0
tellerEind = len(s) - 1

while s[tellerBegin] == s[tellerEind]:
    tellerEind -= 1
    tellerBegin += 1
    if tellerBegin >= tellerEind:
        print(s, "is a palindrome")
        break

else:
    print(s, "is not a palindrome")