palabra=input("palabra: ")

if palabra==palabra[::-1]:
    print( palabra,"is a palindrome")

else:
    print(palabra,"is not a palindrome")
