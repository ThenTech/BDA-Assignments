def create_sequence(string, index, length):
    lengtestring = len(string)
    index = int (index)
    letternr = lengtestring + index
    teruggave = ""
    for i in range (0, length):
        while (lengtestring <= letternr):
            letternr -= lengtestring
        letternr = int(letternr)
        teruggave = teruggave + string[letternr]
    return teruggave