def cleanup_spaces(s):
    sentence = ""
    for letter in s:
        if letter != " " or sentence[len(sentence) - 1:] != " ":
            sentence += letter
    return sentence