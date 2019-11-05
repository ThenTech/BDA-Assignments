cents = int(input("one-cents? "))
cents = cents + 2 * int(input("two-cents? "))
cents = cents + 5 * int(input("five-cents? "))
cents = cents + 10 * int(input("ten-cents? "))
cents = cents + 20 * int(input("twenty-cents? "))

euros = cents // 100

tencents = (cents % 100) // 10
onecents = (cents % 10)

print("You have ", euros, ".", tencents, onecents, " euro!", sep="")
