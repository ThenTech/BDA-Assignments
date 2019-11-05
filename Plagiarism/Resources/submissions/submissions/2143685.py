text = input()
even = 0

for i in range(0, len(text)):
    if (int(text[i]) % 2) == 0:
        even += 1
print(even)
