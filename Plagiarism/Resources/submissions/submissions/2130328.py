# write your code here

x = int(input("Val of x"))

def fac(a):
  fact = 1
  for i in range(1, a+1):
    fact *= i
  return fact

sum_of_val = 0

for val in range(1, x+1):
    sum_of_val += fac(val)
    
print(sum_of_val)