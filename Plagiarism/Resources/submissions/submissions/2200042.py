def find(s, ch):
    x = 0
    while x < len(s):
        if s[x] == ch:
            return x
        x += 1
    return -1

def replace(pattern, replacement, corpus):
    woorden = corpus.split()
    teller = -1
    for element in woorden:
        teller += 1
        if pattern in element:
            if pattern == element:
                woorden[teller] = replacement
            else:
                start = find(element, pattern)
                einde = len(pattern)-start
                woorden[teller] = element[start:0] + replacement + element[einde-1:]
        else:
            continue
    for x in woorden:
        print(x, end=' ')

replace("sean", "steve", "sean,zit naast pim sean")