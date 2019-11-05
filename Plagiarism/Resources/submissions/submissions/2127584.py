n = int(input("Geef aantal eurocenten"))
euro_2 = n // 200
euro_1 = (n % 200) // 100
cent_50 = (n % 100) // 50
cent_20 = (n % 50) // 20
cent_10 = ((n % 50) % 20) // 10
cent_5 = (n % 10) // 5
cent_2 = (n % 5) // 2
cent_1 = ((n % 5) % 2) // 1
print("2-euros:", euro_2)
print("1-euros:", euro_1)
print("50c-euros:", cent_50)
print("20c-euros:", cent_20)
print("10c-euros:", cent_10)
print("5c-euros:", cent_5)
print("2c-euros:", cent_2)
print("1c-euros:", cent_1)