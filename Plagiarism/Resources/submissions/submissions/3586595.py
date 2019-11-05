string = input()

count = 0

for i in range(len(string)):
    if (string[i] % 2 == 0):
        count += 1
        
print(count)