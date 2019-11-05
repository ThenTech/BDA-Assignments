def is_palindrome_sentence(sentence):
    alphabetstring = "abcdefghijklmnopqrstuvwxyz"
    letterlist = []
    isPalindrome = False
    
    for i in sentence:
        if i in alphabetstring:
            letterlist.append(i)
    word = "".join(letterlist)
    
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            isPalindrome = False
            break
        elif word[i] == word[len(word) - i - 1] and i == len(word) - 1:
            isPalindrome = True
    
    return isPalindrome
    pass