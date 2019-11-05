def count_words(string):
    amount = 1
    for c in string:
        if c == " ":
            amount += 1
    return amount
        