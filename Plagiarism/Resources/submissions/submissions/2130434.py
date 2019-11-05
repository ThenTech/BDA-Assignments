n = int(input())
k = int(input())

facultyOfN = 1
facultyOfK = 1
facultyOfNMinusK = 1

for value in range(1, n + 1):
    facultyOfN *= value

for value in range(1, k + 1):
    facultyOfK *= value

for value in range(1, (n-k) + 1):
    facultyOfNMinusK *= value

result = facultyOfN / (facultyOfK * facultyOfNMinusK)

print(int(result))