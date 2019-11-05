def shift(l, n):
    output = []
    for i in range(len(l)):
        output.insert((i + n) % len(l), l[i])
    return output
