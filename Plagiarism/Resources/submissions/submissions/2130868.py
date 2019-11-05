x = int(input())
y = int(input())

output = 1

reverse = x

for i in range(1, y+1):
    output = output*reverse/i
    reverse = reverse - 1
print(str(int(output)))
