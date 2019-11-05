woord = input('Geef je woord in: ')
lengte = len(woord)
lijst = list(woord)
controle = ''
for x in lijst:
    letter = lijst[lengte-1]
    controle = controle + letter
    lengte -= 1
if controle == woord:
    print(woord,'is a palindrome')
else:
    print(woord, 'is not a palindrome')
print()