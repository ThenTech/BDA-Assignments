def create_sequence(string, index, length):
    lenghte = len(string)
    woord =""
    for i in range(index,length+index):
        x= int(i) % lenghte
        woord += string[x]
    return woord
print(create_sequence("word",-3,9))