mport string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def find(s, ch):
    x = 0
    while x < len(s):
        if s[x] == ch:
            return x
        x += 1
    return -1


def replace(pattern, replacement, corpus):
    woorden = remove_punctuation(corpus).split()
    teller = -1
    for element in woorden:
        teller += 1
        if pattern in element:
            if pattern == element:
                woorden[teller] = replacement
            else:
                start = find(element, pattern)
                einde = len(element)-start
                woorden[teller] = woorden[start:einde]



        else:
            continue
    print(woorden)

replace("sean", "steve", "sean zit naast pimsean")