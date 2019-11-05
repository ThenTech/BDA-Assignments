ta = int(input("Vul het te betalen bedrag in: "))
t2e = ta // 200
r = ta % 200
t1e = r // 100
r %= 100
t50c = r // 50
r %= 50
t20c = r // 20
r %= 20
t10c = r // 10
r %= 10
t5c = r // 5
r %= 5
t2c = r // 2
r %= 2
t1c = r // 1
r %= 1
print("2-euros:", t2e)
print("1-euros:", t1e)
print("50c-euros:", t50c)
print("20c-euros:", t20c)
print("10c-euros:", t10c)
print("5c-euros:", t5c)
print("2c-euros:", t2c)
print("1c-euros:", t1c)