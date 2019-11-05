# write your code here
a = int(input("aantal kolommen"))
b = int(input("aantal rijen"))
teller = 1
for value1 in range(b):
    for value2 in range(a):
        print(str(teller) + " ", end="")
        teller += 1
    print("\n")