x = int(input())
y = int(input())
out = 1
for i in range(y):
    out *= ((x-i)/(y-i))
print(int(out))
