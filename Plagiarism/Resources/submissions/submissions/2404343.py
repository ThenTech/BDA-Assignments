def convert(n):
    if len(n) > 0:
        convert(n[0: len(n) - 1])
        print(n[len(n) - 1], end="")