ta = int(input("Vul het te betalen bedrag in: "))
t2e = ta // 200
r = ta % 200
t1e = r // 100
r = r % 100
t50c = r // 50
r = r % 50
t20c = r // 20
r = r % 20
t10c = r // 10
r = r % 10
t5c = r // 5
r = r % 5
t2c = r // 2
r = r % 2
t1c = r // 1
r = r % 1
print("2-euros:", t2e)
print("1-euros:", t1e)
print("20c-euros:", t50c)
print("10c-euros:", t20c)
print("5c-euros:", t10c)
print("2c-euros:", t5c)
print("1c-euros:", t2c)
print("2-euros:", t1c)