inp = int(input())

print('2-euros:', inp//200)
inp = inp % 200

print('1-euros:', inp//100)
inp = inp % 100

print('50c-euros:', inp//50)
inp = inp % 50

print('20c-euros:', inp//20)
inp = inp % 20

print('10c-euros:', inp//10)
inp = inp % 10

print('5c-euros:', inp//5)
inp = inp % 5

print('2c-euros:', inp//2)
inp = inp % 2

print('1c-euros:', inp//1)
inp = inp % 1