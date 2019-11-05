def count_words(abc):
    content : abc.read()
    abc.close()
    amountofwords = content.split
    print(len(amountofwords))