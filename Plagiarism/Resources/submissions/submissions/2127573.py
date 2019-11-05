total = int(input())
euro = total // 100
first_cent = (total % 100) // 10
last_cent = (total % 100) % 10

twoEuros = euro // 2
fifthyCent = first_cent // 5
twentyCent = (first_cent - fifthyCent * 5) // 2
tenCent = first_cent - (fifthyCent * 5) - (twentyCent * 2)
fiveCent = last_cent // 5
twoCent = (last_cent - fiveCent * 5) // 2
oneCent = last_cent - (fiveCent * 5) - (twoCent * 2)
print('2-euros:', twoEuros)
print('1-euros:', (euro - twoEuros *2))
print('50c-euros', fifthyCent)
print('20c-euros', twentyCent)
print('10c-euros', tenCent)
print('5c-euros', fiveCent)
print('2c-euros', twoCent)
print('1c-euros', oneCent)