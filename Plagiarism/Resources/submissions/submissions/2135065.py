sentence = input("write a sentence ")
x = 0
y = 0
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","x","r","s","t","u","v","w","x","y","z"]
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while x < len(sentence):
    for y in range(26):
        if sentence[x] == letters[y]:
            count[y] += 1

    x += 1
for y in range(26):
    print(letters[y], ": ", count[y], sep="")