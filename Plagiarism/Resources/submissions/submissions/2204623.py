def replace(pattern, replacement, corpus):
    woorden = corpus.split()
    teller = -1
    for element in woorden:
        teller += 1
        if pattern in element:
            if pattern == element:
                woorden[teller] = replacement
            else:
                begin = 0
                for i in element:
                    if i == pattern[0]:
                        break
                    else:
                        begin += 1
                        continue
                einde = begin + len(pattern)
                lengtepattern = len(pattern)
                lengtereplacement = len(replacement)
                if lengtepattern >= lengtereplacement:
                    woorden[teller] = element[0:begin] + replacement + element[einde:]
                else:
                    woorden[teller] = element[:begin] + replacement + element[einde:]
        else:
            continue
    uitkomst = ''
    for x in woorden:
        uitkomst += x + ' '
    uitkomst = uitkomst[:len(uitkomst) - 1]

    return uitkomst

print(replace("steve", "sean", "..steve... en steve"))