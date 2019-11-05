word = input()
for i in range(len(word)//2):
    if word[i]!=word[len(word)-i-1]:
        print(word,"is not a palindrome")
        break
    elif i == (len(word)//2)-1:
        print(word,"is a palindrome")