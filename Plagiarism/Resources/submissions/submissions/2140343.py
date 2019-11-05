string1 = input("give me the first string: ")
string2 = input("give me the second and last string: ")
if sorted(string1) == sorted(string2):
    print(string1, "and", string2, "are anagrams")
else:
    print(string1, 'and', string2, "are not anagrams")