text = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, len(alphabet)-1):
    print(alphabet[i] + ": " + str(text.count(alphabet[i])))