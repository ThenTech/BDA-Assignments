response = int(input())

faculty = 0
facultySum = 0

for valueX in range(1, response + 1):
    for valueY in range(1, valueX + 1):
        faculty += valueY
    facultySum += faculty
    faculty = 0

print(int(facultySum))