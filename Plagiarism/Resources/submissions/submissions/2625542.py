word = input()
for i in range(len(word)//2):
    if word[i]!=word[len(word)-i]:
        print(word,"is not a palindrome")
        break
    elif i == len(word)//2:
        print(word,"is a palindrome")