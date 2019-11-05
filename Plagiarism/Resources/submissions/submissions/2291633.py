def fibonacci_values(i):
    A = [0, 1]
    if i == 0:
        print([])
    elif i == 1:
        print([0])
    else:
        for aantal in range(2, i):
            A[aantal] = A[aantal-1] + A[aantal-2]
        print(A)