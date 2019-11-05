x = input("Input your number here")
r = 0
y = input("input2")
for i in range(int(x)+1):
    r = r * ((int(x) - i) / (int(y) - i))
print(int(r))