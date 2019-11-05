import string

alphabet = string.ascii_lowercase

s1 = input("")
s2 = input("")

count = 0
test = True

while count < 26 and test == True:
    if s1.count(alphabet[count]) == s2.count(alphabet[count]):
        test = True
    else:
        test = False
    count += 1

if test == True:
    print(s1, "and", s2, "are anagrams")
else:
    print(s1, "and", s2, "are not anagrams")