word = input()

reverse = word[::-1]

if word.lower() == reverse.lower():
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")