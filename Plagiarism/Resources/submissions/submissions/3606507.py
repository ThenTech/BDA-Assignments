w1 = input()
w2 = input()


def anagram(w1, w2):
    w2 = w2.replace(' ', '')
    w1 = w1.replace(' ', '')
    if (len(w1) != len(w2)):
        return w1 + " and " + w2 + " are not anagrams"
    c_w1 = w1[:]
    for letter in range(len(w2)):
        if w2[letter] not in c_w1:
            return w1 + " and " + w2 + " are not anagrams"
        else:
            temp = c_w1.replace(w2[letter], '', 1)
            c_w1 = temp
    return w1 + " and " + w2 + " are anagrams"


print(anagram(w1, w2))