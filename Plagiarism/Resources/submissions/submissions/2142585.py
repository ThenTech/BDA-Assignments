text = input()
length = len(text)

output = ""
for i in range(1, length+1):
    output += text[length-i]
print(output)
