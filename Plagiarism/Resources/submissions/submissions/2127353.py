cents = int(input("Amount of money: "))

# 2 euro coins
coineur2 = cents // 200
cents = cents % 200

# 1 euro coins
coineur1 = cents // 100
cents = cents % 100

# 50 cent coins
coincent50 = cents // 50
cents = cents % 50

# 20 cent coins
coincent20 = cents // 20
cents = cents % 20

# 10 cent coins
coincent10 = cents // 10
cents = cents % 10

# 5 cent coins
coincent5 = cents // 5
cents = cents % 5

# 2 cent coins
coincent2 = cents // 2
cents = cents % 2

print("2-euros:", coineur2,
      "1-euros:", coineur1,
      "50c-euros:", coincent50,
      "20c-euros:", coincent20,
      "10c-euros:", coincent10,
      "5c-euros:", coincent5,
      "2c-euros:", coincent2,
      "1c-euros:", cents)
# write your code here