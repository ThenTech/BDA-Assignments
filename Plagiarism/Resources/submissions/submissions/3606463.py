# write your code here

x = input()

count = 0
string = ""
for i in range(len(x)):
    if x[i] < 'a' or x[i] > 'z':
        if x[i] < 'A' or x[i] > 'Z':
            if count != 0:
                print(string, count)
        else
            count += 1
            string += x[i]
    else
        count += 1
        string += x[i]
if count != 0:
    print(string, count)