symbols = ['A', 'C', 'G', 'T']


def place_symbol(n, string):
    if n > 0:
        for i in range(4):
            result = string
            result += symbols[i]
            place_symbol(n-1, result)
            if n == 1:
                print(result)


place_symbol(int(input()), "")
