def comb(n):
    L = "ACGT"
    diff(L, n, "")


def diff(string, n, save):
    if len(save) == n:
        print(save)
    else:
        for i in string:
            diff(string, n, save + i)

comb(int(input()))