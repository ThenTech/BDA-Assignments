# write your code here

total = int(input("How many eurocents"))

c200 = total // 200
total -= c200 * 200
c100 = (total) // 100
total -= c100 * 100
c50 = (total) // 50
total -= c50 * 50
c20 = (total) // 20
total -= c20 * 20
c10 = (total) // 10
total -= c10 * 10
c5 = (total) // 5
total -= c5 * 5
c2 = (total) // 2
total -= c2 * 2
c1 = (total) // 1

print("2-euros: " + str(c200))
print("1-euros: " + str(c100))
print("50c-euros: " + str(c50))
print("20c-euros: " + str(c20))
print("10c-euros: " + str(c10))
print("5c-euros: " + str(c5))
print("2c-euros: " + str(c2))
print("1c-euros: " + str(c1))