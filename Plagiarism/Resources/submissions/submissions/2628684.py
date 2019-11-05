def remove_punctuation(string):
    punct = "`~!@1234567890#$%^&:*()_+=-;[]{}\|/?><., "
    stringy = ""
    for i in string+" ":
        if i in punct:
            continue
        else:
            stringy += i
    return stringy


def is_palindrome_sentence(sentence):
    stringy = remove_punctuation(sentence)
    stringy = stringy.lower()
    for i in range(len(stringy)//2):
        if stringy[i] != stringy[len(stringy)-1-i]:
            return False
    return True