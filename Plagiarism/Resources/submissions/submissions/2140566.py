woord = input()

lengtewoord = len(woord)
ispalindrome = True
teller = 0

while ispalindrome and teller < lengtewoord / 2:
    if woord[teller] == woord[lengtewoord - 1 - teller]:
       teller += 1
    else:
        ispalindrome = False
        print(woord, "is not a palindrome")
        
if ispalindrome:
    print(woord, "is a palindrome")

            