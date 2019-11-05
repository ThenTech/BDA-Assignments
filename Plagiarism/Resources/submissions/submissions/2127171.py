# write your code here

total = int(input("How many eurocents"))

c200 = total // 200
c100 = (total - c200 * 200) // 100
c50 = (total - c100 * 100) // 50
c20 = (total - c50 * 50) // 20
c10 = (total - c20 * 20) // 10
c5 = (total - c10 * 10) // 5
c2 = (total - c5 * 5) // 2
c1 = (total - c2 * 2) // 1

print("2-euros: " + str(c200))
print("1-euros: " + str(c100))
print("50c-euros: " + str(c50))
print("20c-euros: " + str(c20))
print("10c-euros: " + str(c10))
print("5c-euros: " + str(c5))
print("2c-euros: " + str(c2))
print("1c-euros: " + str(c1))
