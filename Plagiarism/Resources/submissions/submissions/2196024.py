def cleanup_spaces(sentence):
    newSentence = ""
    for i in range(1, len(sentence) + 1):
        if sentence[i-1] == " " and sentence[i] == " ":
            newSentence += ""
        else:
            newSentence += sentence[i-1]

    while newSentence[0] == " ":
        newSentence = newSentence[1:]
    return newSentence

