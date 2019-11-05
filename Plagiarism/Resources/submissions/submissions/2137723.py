s = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ammount  = 11111111111111111111111111

for i in range(len(s)):
    for j in range(len(alphabet)):
        if s[i] == alphabet[j]:
            ammount += 10**(25-j)
            break;

ammount = str(ammount)
for x in range(len(ammount)):
    print(alphabet[x], ': ', int(ammount[x])-1, sep='')