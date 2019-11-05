zin = input()
alfabet = "abcdefghijklmnopqrstuvwxyz"
for i in alfabet:
    teller = 0
    for j in zin:
        if i == j:
            teller += 1
    print(i+":",teller)