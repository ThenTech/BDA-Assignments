sentence = inp()
counter = 0
for i in sentence:
    if 96 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
        print(i)
        counter += 1
    elif counter != 0:
        print(" ", counter) 
        counter = 0