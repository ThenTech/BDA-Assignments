string = str(input())
aantal =0
for i in string:
    if int(i) % 2 ==0:
        aantal += 1
print(aantal)