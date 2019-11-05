string = input()

alphabetLocation =  0
letter = 97

list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(string)):
    if string[i] != " ":
        alphabetLocation = ord(string[i]) - 97
        list[alphabetLocation] += 1
    
for i in list:
    print(chr(letter), ": ", i, sep="")
    letter += 1