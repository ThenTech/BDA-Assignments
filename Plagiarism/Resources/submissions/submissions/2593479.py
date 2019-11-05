cents = int(input())

print('2-euros:', cents// 200)
cents = cents % 200

print('1-euros:', cents// 100)
cents = cents % 100

print('50c-euros:', cents// 50)
cents = cents % 50

print('20c-euros:', cents// 20)
cents = cents % 20

print('10c-euros:', cents// 10)
cents = cents % 10

print('5c-euros:', cents// 5)
cents = cents % 5

print('2c-euros:', cents// 2)
cents = cents % 2

print('1c-euros:', cents)