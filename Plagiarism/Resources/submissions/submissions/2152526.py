day = 15
month = 3
year = -124
dayt = 8
montht = 9
yeart = -59

month *= 30
year *= 365
day = day + month + year

montht *= 30
yeart *= 365
dayt = dayt + montht + yeart

day = dayt - day

age = day // 365

print(age)