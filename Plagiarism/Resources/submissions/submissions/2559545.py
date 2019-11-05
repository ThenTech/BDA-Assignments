cents = int(input("1cent? "))
cents = cents + 2 * int(input("2cent? "))
cents = cents + 5 * int(input("5cent? "))
cents = cents + 10 * int(input("10cent? "))
cents = cents + 20 * int(input("20cent? "))
euros = cents // 100
tencents = (cents % 100) // 10
onecents = (cents % 10)
print("You have ", euros, ".",
      tencents, onecents, " euro!", sep="")