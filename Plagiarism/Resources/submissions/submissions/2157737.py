def create_sequence(string, index, length):
    lenghte_string = len(string)
    index_abs = index
    uitkomst = ""
    lenghte_uitkomst = len(uitkomst)
    teller = 0
    for i in range(0, length):
        if int(index) < 0:
            teller = i+lengthe_string
        if index> lenghte_string:
            teller = i - lengthe_string
        uitkomst += string[teller]
        teller +=1
    return uitkomst