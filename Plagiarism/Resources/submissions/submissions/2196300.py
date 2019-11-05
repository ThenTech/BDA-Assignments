def count_words(text):
    filterText = ""
    for char in text:
        if char in "!,1234567890":
            filterText += " "
        else:
            filterText += char

    splitedFiltered = filterText.split()
    return len(splitedFiltered)