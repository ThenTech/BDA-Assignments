def is_palindrome_sentence(s):
    output = ""
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~“”’"
    numbers = "1234567890"
    for letter in s:
        if letter in punctuation:
            s = s.replace(letter, "")
    for letter in s:
        if letter in numbers:
            s = s.replace(letter, "")
    s = s.lower()
    s = s.replace(" ", "")
    for i in range(len(s)):
        backwards = s[len(s) - 1 - i]
        output += backwards
    return bool(output == s)