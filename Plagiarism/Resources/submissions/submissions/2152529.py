day = int(input())
month = int(input())
year = int(input())
dayt = int(input())
montht = int(input())
yeart = int(input())

month *= 30
year *= 365
day = day + month + year

montht *= 30
yeart *= 365
dayt = dayt + montht + yeart

day = dayt - day

age = day // 365

print(age)