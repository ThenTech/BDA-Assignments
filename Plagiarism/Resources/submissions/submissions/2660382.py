def combi(n):
    nucleo = "ACGT"
    recur(nucleo, n, "")
    return

def recur(nucleo, n, result):
    if n == 0:
        print(result)
        return
    for i in nucleo:
        recur(nucleo, n-1, result + i)
    return
