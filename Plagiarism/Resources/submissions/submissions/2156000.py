def create_sequence(string, index, length):
    lengtestring = len(string)
    index = float index
    letternr = lengtestring + index
    teruggave = ""
    for i in range (0, length):
        while lengtestring <= letternr:
            letternr -= lengtestring
        teruggave += string[letternr]
    return teruggave