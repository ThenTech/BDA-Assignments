# write your code here

money = int(input("How much money do you have to pay in eurocents? "))
euros_2 = money // 200
euros_1 = (money - euros_2*200) // 100
euros_50c = (money - euros_2*200 - euros_1*100) // 50
euros_20c = (money - euros_2*200 - euros_1*100 - euros_50c*50) // 20
euros_10c = (money - euros_2*200 - euros_1*100 - euros_50c*50 - euros_20c*20) // 10
euros_5c = (money - euros_2*200 - euros_1*100 - euros_50c*50 - euros_20c*20 - euros_10c*10) // 5
euros_2c = (money - euros_2*200 - euros_1*100 - euros_50c*50 - euros_20c*20 - euros_10c*10 - euros_5c*5) // 2
euros_1c = (money - euros_2*200 - euros_1*100 - euros_50c*50 - euros_20c*2 - euros_10c*10 - euros_5c*5 - euros_2c*2)

print("2-euros:", euros_2)
print("1-euros:", euros_1)
print("50c-euros:", euros_50c)
print("20c-euros:", euros_20c)
print("10c-euros:", euros_10c)
print("5c-euros:", euros_5c)
print("2c-euros:", euros_2c)
print("1c-euros:", euros_1c)