cents = int(input("Give an amount of money in eurocents:"))

n_2 = cents // 200
new_cents = cents - (n_2 * 200)
print("2-euros: ", n_2)

n_1 = new_cents // 100
new_cents = new_cents - (n_1 * 100)
print("1-euros: ", n_1)

n_50 = new_cents // 50
new_cents = new_cents - (n_50 * 50)
print("50c-euros: ", n_50)

n_20 = new_cents // 20
new_cents = new_cents - (n_20 * 20)
print("20c-euros: ", n_20)

n_10 = new_cents // 10
new_cents = new_cents - (n_10 * 10)
print("10c-euros: ", n_10)

n_5 = new_cents // 5
new_cents = new_cents - (n_5 * 5)
print("5c-euros: ", n_5)

n_2c= new_cents // 2
new_cents = new_cents - (n_2c * 2)
print("2c-euros: ", n_2c)

n_1c = new_cents // 1
new_cents = new_cents - (n_1c * 1)
print("1c-euros: ", n_1c)