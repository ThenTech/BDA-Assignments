def verwerken(input, result = ""):
    if input < 1:
        return result
    for i in ["A", "C", "G", "T"]:
        result5 = result
        result5 += i
        output = verwerken(input-1, result5)
        if output is not None:
            print(output)