def is_palindrome_sentence(sentence):
    sentence_word = ""

    for char in sentence:
        if char in "123456789&é"'(§è!çà) -_,;:=?./+¨*%£^$ùµ<>\~´`[]|@#^{}/*-+':
            sentence_word += ""
        else:
            sentence_word += char
    return sentence_word.lower()


w = is_palindrome_sentence("A man, a plan, not a canal: Panama.")

mirror = ""

for i in range(0, len(w)):
    mirror = w[i] + mirror

if w == mirror:
    print("True")
else:
    print("False")
