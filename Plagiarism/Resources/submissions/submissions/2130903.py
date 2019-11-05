# write your code here
response = input("What is the n")
n = int(response)
r = 1

for i in range(1, n+1):
    r = r * i
r = r + i
print(r)