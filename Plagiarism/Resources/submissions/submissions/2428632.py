s = input( "Type in your word you want to reverse")
for i in range(len(s)):
    print(s[len(s)-1-i], end="")
    print()