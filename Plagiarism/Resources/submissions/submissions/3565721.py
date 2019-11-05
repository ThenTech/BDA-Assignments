def convert_to_simple_string(sent):
    new_sent = sent.lower()
    newer_sent = ""
    for i in new_sent:
        if i in string.ascii_letters:
            newer_sent += i
    return newer_sent


def is_palindrome_sentence(sentence):
    first = convert_to_simple_string(sentence)
    second = ""
    for i in range(len(first)):
        second += first[-i -1]
    print(first, "<->", second)
    return first == second