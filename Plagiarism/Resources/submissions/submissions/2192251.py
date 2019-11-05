def is_palindrome_sentence(sentence):
    niet = ",?;.:/<>[]^!" "
    oudezonderspaties = ""
    nieuwe = ""
    nieuwezonderspaties = ""
    teller = 0
    for i in sentence:
        if i in niet:
            continue
        else:
            oudezonderspaties += i

    while teller < len(sentence):
        nieuwe += sentence[len(sentence)-teller-1]
        teller += 1

    for i in nieuwe:
        if i in niet:
            continue
        else:
            nieuwezonderspaties += i

    oudezonderspaties = oudezonderspaties.lower()
    nieuwezonderspaties = nieuwezonderspaties.lower()

    if oudezonderspaties == nieuwezonderspaties:
        return True
    else:
        return False