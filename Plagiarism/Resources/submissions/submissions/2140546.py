word = input()

lengteword = len(word)
ispalindrome = True
teller = 0

while ispalindrome and teller < lengtewoord / 2:
   if word[teller] == word[lengteword - 1 - teller]:
       teller += 1
    else:
        ispalindrome = false
        print(word, "is not a palindrome")
print(word, "is a palindrome")

            