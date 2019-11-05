def is_palindrome_sentence(sentence):
    filterText = ""
    for char in sentence:
        if char not in "!?”“’;',:. ":
            filterText += char

    counter = 0
    is_palindrome = True
    for char in filterText.lower():
        if filterText[counter].lower() != filterText[len(filterText) - counter - 1].lower():
            is_palindrome = False
            break

        counter += 1

    return is_palindrome

print(is_palindrome_sentence("Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era."))