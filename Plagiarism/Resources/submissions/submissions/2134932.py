word = input()

reverse = word[::-1]

if word == reverse:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")