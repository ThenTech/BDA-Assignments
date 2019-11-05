def create_sequence(string, index, length):
    lenghte_string = len(string)
    index_abs = index
    uitkomst = ""
    lenghte_uitkomst = len(uitkomst)
    teller = 0
    for i in range(0, length):
        uitkomst += string[index]
        index +=1
    return uitkomst