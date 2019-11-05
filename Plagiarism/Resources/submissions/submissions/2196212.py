def cleanup_spaces(sentence):
    newSentence = ""

    while sentence[0] == " ":
        sentence = sentence[1:]

    while sentence[len(sentence)-1] == " ":
        sentence = sentence[:int(len(sentence)-1)]

    for i in range(0, len(sentence)):
        if sentence[i] == " " and sentence[i+1] == " ":
            newSentence += ""
        else:
            newSentence += sentence[i]

    return newSentence