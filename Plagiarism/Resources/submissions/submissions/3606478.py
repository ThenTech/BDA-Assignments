# write your code here

x = input()

count = 0
string = ""
for i in (x):
    if i < 'a' or i > 'z':
        if i < 'A' or i > 'Z':
            if count != 0:
                print(string, count)
                count = 0
                string = 0
        else:
            count += 1
            string += (char)i
    else:
        count += 1
        string += (char)i
if count != 0:
    print(string, count)