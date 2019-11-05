amount = int(input("geef aantal eurocenten in: "))

tweeEuro = amount // 200
eenEuro = int(amount % 200 / 100)
vijftigCent = int(amount % 200 % 100 / 50)
twintigCent = int(amount % 200 % 100 % 50 / 20)
tienCent = int(amount % 200 % 100 % 50 % 20 / 10)
vijfCent = int(amount % 200 % 100 % 50 % 20 % 10 / 5)
tweeCent = int(amount % 200 % 100 % 50 % 20 % 10 % 5 / 2)
eenCent = int(amount % 200 % 100 % 50 % 20 % 10 % 5 % 2)

print("2-euros:", str(tweeEuro) + "\n" +
      "1-euros:", str(eenEuro) + "\n" +
      "50c-euros:", str(vijftigCent) + "\n" +
      "20c-euros:", str(twintigCent) + "\n" +
      "10c-euros:", str(tienCent) + "\n" +
      "5c-euros:", str(vijfCent) + "\n" +
      "2c-euros:", str(tweeCent) + "\n" +
      "1c-euros:", str(eenCent))
