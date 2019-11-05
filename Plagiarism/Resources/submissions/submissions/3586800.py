def create_sequence(string, index, length):
    stringA = (length + index) * string
    
    if index > 0:
        return stringA[2*len(string)+index:length+index]
    else:
        return stringA[2*len(string)+index:length-index]

    