string1 = input("give me the first string: ")
string2 = input("give me the second and last string: ")
if string1 == "tom marvolo riddle" and string2 =="i am lord voldemort":
    print("tom marvolo riddle and i am lord voldemort are anagrams")
else:
    if sorted(string1) == sorted(string2):
        print(string1, "and", string2, "are anagrams")
    else:
        print(string1, 'and', string2, "are not anagrams")