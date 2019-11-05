numb = input("Geef een getal groter dan 0 in : ")
count = 0

for x in range(0,len(numb)):
    if int(numb[x])% 2 == 0:
        count += 1
print(count)