def palindrome(str):
    for i in range(len(str)//2):
        if (str[i] != str[len(str)-1-i]):
            return (str + " is not a palindrome")
    return (str + " is a palindrome")

print(palindrome(input()))