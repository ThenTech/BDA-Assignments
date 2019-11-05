string = input()

count = 0

for i in range(len(string)):
    if (ord(string[i]) - 48) % 2 == 0:
        count += 1
        
print(count)