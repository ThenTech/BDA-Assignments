w1 = input()
w2 = input()


def anagram(a, b):
    w2 = b.replace(' ', '')
    w1 = a.replace(' ', '')
    if (len(w1) != len(w2)):
        return a + " and " + b + " are not anagrams"
    c_w1 = w1[:]
    for letter in range(len(w2)):
        if w2[letter] not in c_w1:
            return a + " and " + b + " are not anagrams"
        else:
            temp = c_w1.replace(w2[letter], '', 1)
            c_w1 = temp
    return a + " and " + b + " are anagrams"


print(anagram(w1, w2))