n = int(input("n:"))
newsom = 0
while n != 0:
    som = n
    for i in range(1, n):
        som += (n-i)
    newsom += som
    n -= 1
print(newsom)