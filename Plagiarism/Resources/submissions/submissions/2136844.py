# write your code here

sentence = input("Geef een zin in: ")

for i in "abcdefghijklmnopqrstuvwxyz":
    count = 0
    for j in sentence:
        if i == j:
            count += 1
    print(i + ": " + str(count))

