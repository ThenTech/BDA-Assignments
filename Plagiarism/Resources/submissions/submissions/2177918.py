x = input("Input your number here")
r = 1
y = input("input2")
for i in range(0, int(y)):
    r = r * ((int(x) - i) / (int(y) - i))
print(int(r))# write your code here