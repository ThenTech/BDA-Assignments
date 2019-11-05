title = input()

count = int(len(title))
stars = ""

print(title + "\n")

for x in range(count):
    stars += "*"

print(stars)