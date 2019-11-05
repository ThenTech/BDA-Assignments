x = int(input("x:"))
y = int(input("y:"))

maal = x * y
for i in range(maal):
      if ((i + 1) % x) == 0:
            print(i + 1)
      else:
            print(i + 1, end=" ")