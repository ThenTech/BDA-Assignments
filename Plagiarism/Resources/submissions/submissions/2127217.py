tb = int(input('Hoeveel euro moet je betalen in eurocent? '))
print('2-euros:', tb//200)
over = tb%200
print('1-euros:', over//100)
over = over%100
print('50c-euros:', over//50)
over = over%50
print('20c-euros:', over//20)
over = over%20
print('10c-euros:', over//10)
over = over%10
print('5c-euros:', over//5)
over = over%5
print('2c-euros:', over//2)
over = over%2
print('1c-euros:', over//1)
