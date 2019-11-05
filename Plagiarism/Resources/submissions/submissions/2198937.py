def filterText(sentence):
    filterText = ""
    for char in sentence:
        foundJunk = False
        for junk in "!?”“’;',:.0123456789":
            if junk == char:
                foundJunk = True
                break

        if foundJunk:
            filterText += ""
        else:
            filterText += char
    word = ""
    counter = 0
    for char in filterText:
        if counter >= len(filterText) - 1:
            word += char
            print(word, len(word))
            word = ""
        else:
            if char != " ":
                word += char
            elif len(word) > 0:
                print(word, len(word))
                word = ""
            counter += 1


filterText(input())
