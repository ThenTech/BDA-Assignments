response = int(input())

faculty = 1

for value in range(1, response + 1):
    faculty *= value

print(int(faculty))