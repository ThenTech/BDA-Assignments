def is_palindrome_sentence(s):
    s = s.lower()
    letter_list = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    string1 = ''
    string2 = ''
    for i in range(len(s)):
        if s[len(s)-i-1] in letter_list:
            string2 += s[len(s) - i -1]
        if s[i] in letter_list:
            string1 += s[i]
    return string1 == string2