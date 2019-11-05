def create_sequence(string, index, length):
    lenghte = len(string)
    aantal = int(length) - int(index)
    woord =""
    for i in range(index,length+1):
        x= int(i) % lenghte
        woord += string[x]
    return woord
print(create_sequence("word",-3,9))