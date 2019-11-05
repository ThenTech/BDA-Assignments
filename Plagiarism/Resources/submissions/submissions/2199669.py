sentence = input("Give a sentence ")
sentence_without_punct = ""
for char in sentence:
    if char in "“”123456789&é"'(§è!çà) -_’,;:=?./+¨*%£^$ùµ<>\~´`[]|@#^{}/*-+':
        sentence_without_punct += " "
    else:
        sentence_without_punct += char
splitsentence = sentence_without_punct.split()
for i in range(len(splitsentence)):
    print(splitsentence[i], len(splitsentence[i]))
