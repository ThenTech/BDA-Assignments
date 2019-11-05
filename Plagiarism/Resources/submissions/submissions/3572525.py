# write your codehere
word = input()

list = []
for i in range(len(word)):
    list.append(word[i])
list.reverse()

omg = ""
for i in range(len(word)):
    omg += list[i]

if list == omg:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")