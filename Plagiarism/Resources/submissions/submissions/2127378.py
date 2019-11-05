# Reading input
cents = int(input("one-cents? "))
cents = cents + 2 * int(input("two-cents? "))
cents = cents + 5 * int(input("five-cents? "))
cents = cents + 10 * int(input("ten-cents? "))
cents = cents + 20 * int(input("twenty-cents? "))

# Writing output: 100 cent per euro
euros = cents // 100

# We calculate the first and second digit after the comma
# seperately, do not want 1.5 in stead of 1.05!
tencents = (cents % 100) // 10
onecents = (cents % 10)

# Output
print("You have ", euros, ".",
      tencents, onecents, " euro!", sep="")
# write your code here