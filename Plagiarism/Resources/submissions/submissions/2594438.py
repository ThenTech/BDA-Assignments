def create_sequence(string, index, length):
    uitvoer = ""
    for i in range(index, index + length):
        x = i % len(string)
        uitvoer += string[x]
        return uitvoer