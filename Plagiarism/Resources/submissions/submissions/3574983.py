# write your code here
x = input()
in_word = False
length = 0
string = ""
for i in x:
    if i.isalpha():
        in_word = True
        length += 1
        string += i
    else:
        if in_word:
            in_word = False
            print(string, length)
            string = ""
            length = 0
print(string, length)
    