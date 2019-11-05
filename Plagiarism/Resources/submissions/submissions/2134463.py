title = input()

count = int(len(title))
stars = ""

print(title)

for x in range(count):
    stars += "*"

print(stars)