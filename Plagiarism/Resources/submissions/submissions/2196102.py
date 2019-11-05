def count_words(string):
    alfabet="azertyuiopqsdfghjklmwxcvbn"
    string = string.lower()
    string = string.split()
    aantal_woorden = 0
    for el in string:
        teller = 0
        while teller < len(el):
           if not el[teller] in alfabet:
               teller = len(el)+1
           else:
               teller = teller + 1
           if teller == len(el):
                aantal_woorden = aantal_woorden + 1

    return aantal_woorden

print(count_words("hallo   j"))