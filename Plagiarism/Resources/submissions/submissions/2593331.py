nummer = input("Geef jouw getal")
count = 0
for i in nummer:
    if i % 2 == 0:
        count += 1
print(count)