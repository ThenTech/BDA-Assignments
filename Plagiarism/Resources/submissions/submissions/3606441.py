fcol = int(input())
frow = int(input())
number = 0
for row in range(frow):
    for col in range(fcol):
        number += 1
        print(number, end=" ")
    print()
        