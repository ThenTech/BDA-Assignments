input = input()
n = len(input)
palindrome = ""

for i in range(len(input)):
    n = n - 1
    palindrome = palindrome + input[n]

if palindrome == input:
    print(input, "is a palindrome")
else:
    print(input, "is not a palindrome")