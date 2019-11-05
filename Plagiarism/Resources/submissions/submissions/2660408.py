def sum(max, lenght, solution):
    if len(solution) == lenght:
        print(solution)
    elif lenght > 0:
        for i in range(max):
            new_solution = solution + [max-i]
            number = max - 1 - i
            sum(number, lenght, new_solution)



def sum_helper(max, lenght):
    sum(max, lenght,[])

x = int(input())
y = int(input())
sum_helper(x, y)