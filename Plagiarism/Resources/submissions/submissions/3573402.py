def fibonacci_values(n):
    last = 0
    current = 1
    next = 1
    output = []
    if n == 1:
        output.append(last)
        return output
    for i in range(1, n):
        next = last + current
        output.append(next)
        last = current
        current = next
    return output
        
    