def is_palindrome_sentence(sentence):
    sentence_word = ""

    for char in sentence:
        if char in "123456789&é"'(§è!çà) -_,;:=?./+¨*%£^$ùµ<>\~´`[]|@#^{}/*-+':
            sentence_word += ""
        else:
            sentence_word += char
    sentence_word_lower = sentence_word.lower()


    mirror = ""

    for i in range(0, len(sentence_word_lower)):
        mirror = sentence_word_lower[i] + mirror

    if sentence_word_lower == mirror:
        return True
    else:
        return False

print(is_palindrome_sentence("A man, a plan, not a canal: Panama."))
