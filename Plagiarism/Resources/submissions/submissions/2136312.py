# write your code here
woord = str(input())
lengthe = len(woord)
i=0
while i<lengthe:
    if woord[i]!=woord[lengthe-1-i]:
        print(woord, "is not a palindrom")
        break
    elif i+1==lengthe:
        print(woord, "is a palindrome")
        i+=1
    else:
        i+=1