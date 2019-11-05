# write your code here

a1cent = int(input())
a2cent = int(input())
a5cent = int(input())
a10cent = int(input())
a20cent = int(input())


total = a1cent + 2*a2cent + 5*a5cent + 10*a10cent + 20*a20cent

beuro = total//100
b10cent = (total%100)//10
b1cent = total%10

print('You have ', beuro, '.', b10cent, b1cent, ' euro!', sep='')




