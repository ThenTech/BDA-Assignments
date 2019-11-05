def fibonacci_values(n):
    last = 0
    current = 1
    output = []
    if n == 1:
        output.append(last)
        return output
    output.append(last)
    output.append(current)
    for i in range(2, n):
        next = last + current
        output.append(next)
        last = current
        current = next
    return output