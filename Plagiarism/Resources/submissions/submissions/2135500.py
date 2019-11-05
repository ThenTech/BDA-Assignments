s = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ammount  = 10000000000000000000000000

for i in range(len(s)):
    for j in range(len(alphabet)):
        if s[i] == alphabet[j]:
            ammount += 10**(25-j)
            break;

ammount = str(ammount-10000000000000000000000000)
for x in range(len(ammount)):
    print(alphabet[x],': ',ammount[x], sep='')
