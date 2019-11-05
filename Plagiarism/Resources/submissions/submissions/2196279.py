def count_words(text):
    filterText = ""
    for char in text:
        if char in "!,1234567890":
            filterText += " "
        else:
            filterText += char

    splitedFiltered = filterText.split()
    print(len(splitedFiltered))

count_words("one two")
count_words("five 6 seven,eight!nine")