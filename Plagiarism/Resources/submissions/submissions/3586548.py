string = input()

alphabetLocation =  0
letter = 97

list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(string)-1):
    alphabetLocation = 97 - string[i]
    list[alphabetLocation] += 1
    
for i in list:
    print(char(letter), ": ", i)
    letter += 1