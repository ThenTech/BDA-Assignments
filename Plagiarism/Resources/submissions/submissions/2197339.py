def is_palindrome_sentence(sentence):
    filterText = ""
    for char in sentence:
        if char not in "!,:. ":
            filterText += char

    counter = 0
    is_palindrome = True
    for char in filterText.lower():
        if filterText[counter].lower() != filterText[len(filterText) - counter - 1].lower():
            is_palindrome = False
            break

        counter += 1

    return is_palindrome

is_palindrome_sentence("A man, a plan, a canal: Panama.")