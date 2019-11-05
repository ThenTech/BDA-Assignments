a = 0
lengte = 0
word = input()
while lengte < len(word):
    for value in [a]:
        if word[len(word) - 1 - lengte] == str(value):
            value += 1
    lengte += 1
for letter in  [a]:
    print(str(letter) + ": " + str(int(letter)))