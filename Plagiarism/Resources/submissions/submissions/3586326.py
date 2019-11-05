money = int(input())
list = [200, 100, 50, 20, 10, 5, 2, 1]
listString = ["2", "1", "50c", "20c", "10c", "5c", "2c", "1c"]

for i in range (len(list)):
    tempMoney = money // list[i]
    print(listString[i], "-euros: ", tempMoney, sep="")
    money -= tempMoney * list[i]
