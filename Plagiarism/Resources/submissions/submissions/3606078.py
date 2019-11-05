def is_palindrome_sentence(sentence):
    alphabetstring = "abcdefghijklmnopqrstuvwxyz"
    letterlist = []
    isPalindrome = False
    lowersentence = sentence.lower()
    
    for i in lowersentence:
        if i in alphabetstring:
            letterlist.append(i)
    word = "".join(letterlist)
    
    for i in range(0, len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            break
        elif i == (len(word) // 2) - 1 and word[i] == word[len(word) - 1 - i]:
            isPalindrome = True
    return isPalindrome
    pass