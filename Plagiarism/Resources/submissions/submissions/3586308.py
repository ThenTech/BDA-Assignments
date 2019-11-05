money = int(input())
list = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
listString = ["2", "1", "50c", "20c", "10c", "5c", "2c", "1c"]

for i in (len(list)-1):
    tempMoney = money // list[i]
    print(listString[i], "-euros: ", tempMoney)
    money -= tempmoney