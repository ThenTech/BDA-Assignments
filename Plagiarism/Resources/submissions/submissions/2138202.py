word = input("Enter your word: \n")

sum = 0

for i in range(len(word)):
    if int(word[i]) % 2 == 0:
        sum += 1

print(sum)
