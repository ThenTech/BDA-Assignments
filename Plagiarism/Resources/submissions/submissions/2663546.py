# write your code here
# write your code here
inputstr = input("word?/sentence?")
inputstr2 = input("word?/sentence?")
letters = "abcdefghijklmnopqrstuvwxyz"
list1 =[]
for characters in letters:
    if characters in inputstr:
        countchar = inputstr.count(characters)
        list1.append(countchar)
    else:
        list1.append('0')
list2 = []
for characters in letters:
    if characters in inputstr2:
        countchar2 = inputstr2.count(characters)
        list2.append(countchar2)
    else:
        list2.append('0')
if list1 == list2:
    print(inputstr, 'and', inputstr2, 'are anagrams')
else:
    print(inputstr, 'and', inputstr2, 'are not anagrams')