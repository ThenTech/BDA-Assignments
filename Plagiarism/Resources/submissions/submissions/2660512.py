gehad = []
def combi(n):
    recur(n, "")
    return


def recur(string, result):
    if string == "":
        if result not in gehad:
            gehad.append(result)
            print(result)
        return
    else:
        recur(string[2:], result)
        recur(string[2:], result+string[0]+" ")
    return


combi(input())
