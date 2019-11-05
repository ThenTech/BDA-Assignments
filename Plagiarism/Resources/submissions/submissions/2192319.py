def is_palindrome_sentence(sentence):
    char_to_delete = ""
    for i in range(32, 65):
        char_to_delete += chr(i)
    for i in range(91, 97):
        char_to_delete += chr(i)
    for i in range(123, 127):
        char_to_delete += chr(i)

    new_sentence = ""
    reversed_new_sentence = ""

    index = -1

    for char in sentence:
        print(char, char in char_to_delete)
        if char not in char_to_delete:
                new_sentence += char
    new_sentence = new_sentence.lower()

    for char in new_sentence:
        reversed_new_sentence += new_sentence[index]
        index -= 1

    if new_sentence == reversed_new_sentence:
        return True
    else:
        return False