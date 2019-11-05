def verwerken(input, result=""):
    if len(input) <= 1:
        return result
    for i in input:
        result5 = result
        result5 += i
        output = verwerken(input[2:], result5)
        if output is None or output[0] == " ":
            continue
        else:
            print(output)
    return


input = input("")
verwerken(input)