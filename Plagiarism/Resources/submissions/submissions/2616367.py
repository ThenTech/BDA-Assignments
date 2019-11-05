nummers = input("fix nummer: ")
count = 0
for i in nummers:
    if int(i)%2==0:
        count += 1
print(count)