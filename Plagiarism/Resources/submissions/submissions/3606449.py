w1 = input()
w2 = input()

def anagram(w1, w2):
    for letter in w2:
        if letter not in w1:
            return w1 + " and " + w2 + " are anagrams"
    return w1 + " and " + w2 + " are not anagrams"
    
anagram(w1, w2)