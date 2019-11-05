s = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ammount  = 10000000000000000000000000

for i in range(len(s)):
    for j in range(len(alphabet)):
        if s[i] == alphabet[j]:
            ammount += 10**(25-j)
            break;

ammount = str(ammount)
for x in range(len(ammount)):
    if x == 0:
        print(alphabet[x], ': ', int(ammount[x]-1), sep='')
    else
        print(alphabet[x],': ',ammount[x], sep='')