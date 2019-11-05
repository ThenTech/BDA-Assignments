def is_palindrome_sentence(sentence):
    string=""
    palindrome=""
    for i in sentence:
        if i in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN":
            string+=i
    string_upper = string.upper()
    for i in range(len(string_upper)):
        palindrome += string_upper[len(string_upper) - 1 - i]
    if palindrome == string_upper:
        return True
    else:
        return False