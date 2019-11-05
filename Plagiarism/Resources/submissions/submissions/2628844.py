def check_word(word, corpus, counter):
    if corpus[counter:counter+len(word)] == word:
        return True
    else:
        return False

def find_word(word, corpus):
    # we maken een lijst met de posities van de overeenkomsten
    # dit door elke letter in de corpus af te gaan, bij een match gaat een andere functie kijken of deze eerste letter match idd een woord-match is
    counter = 0
    listy = []
    for i in range(len(corpus)):
        if corpus[i] == word[0]:
            if check_word(word, corpus, counter) == True:
                listy.append(counter)
                counter += 1
        else:
            counter += 1
    return listy

def replace(pattern, replacement, corpus):
    listy = find_word(pattern, corpus)
    new_corpus = ""
    start = 0
    j = 0
    i = 0
    while j < len(corpus):
        if i < len(listy) and j == listy[i]:
            new_corpus += replacement
            j += len(pattern)-1
            i += 1
        else:
            new_corpus += corpus[j]
        j += 1
    return new_corpus

