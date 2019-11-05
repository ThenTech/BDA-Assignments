def create_sequence(string, index, length):
    stringA = (length + index) * string
        
    return stringA[2*len(string)-index:length]
    
    