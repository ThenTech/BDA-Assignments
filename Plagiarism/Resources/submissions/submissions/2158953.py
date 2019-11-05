def create_sequence(string, index, length):
    lenghte_string = len(string)
    uitkomst = ""
    lenghte_uitkomst = len(uitkomst)
    teller = 0
    for i in range(0, length):
        if int(index) >= lenghte_string:
            index = index-lenghte_string
        if int(index) <= -lenghte_string:
            index = index + lenghte_string
        uitkomst += string[index]
        index +=1
    return uitkomst
print(create_sequence("word",-5,15))