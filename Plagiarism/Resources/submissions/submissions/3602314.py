# write your code here
given_string = input("Give me a sentence")
alphabetstring = "abcdefghijklmnopqrstuvwxyz"
countarray = [x * 0 for x in range(26)]

for letter in given_string:
    for i in range(26):
        if alphabetstring[i] == letter:
            countarray[i] += 1
            break
        else: 
            continue

for i in range(26):
    print(alphabetstring[i], ": ", countarray[i], sep="")

