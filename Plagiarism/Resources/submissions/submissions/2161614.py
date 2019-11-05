def create_sequence(string, index, length):
    Output = string
    LargeString = string * length
    Output = Output[index:]
    for j in range(length - len(string) + 1):
        Output += LargeString[j]
    return Output



print(create_sequence("programming is fun", 2, 12))
