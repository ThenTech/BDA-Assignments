# write your codehere
word = input()

list = []
for i in word:
    list.append(i)
list.reverse()

omg = ""
for i in list:
    omg += i

if list == omg:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")