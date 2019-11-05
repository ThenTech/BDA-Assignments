# write your code here

x = int(input("Val of x:"))

def fac(a):
  fact = 1
  for i in range(1, a+1):
    fact *= i
  return fact

print(fac(x))