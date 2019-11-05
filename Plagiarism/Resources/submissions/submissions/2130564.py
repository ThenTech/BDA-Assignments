# write your code here
rij= int(input())
kolom= int(input())
uitkomst = 1
value= 0
for value in range(int(kolom)):
    for value in range(rij):
        print(uitkomst, end=" ")
        uitkomst+=1
        value+=1
    print()
    value=0