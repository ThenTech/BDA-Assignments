def filter(s):
    new_s = ""
    for i in range(len(s)):
        if "A" <= s[i] <= "Z":
            new_s += char(ord("a") + ord(s[i]) - ord("A"))
        elif "a" <= s[i] <= "z":
            new_s += s[i]
    return new_s

def mirror(string):
    mirror_string = ""
    for i in range(len(string)):
        mirror_string += string[len(string) - 1 - i]
    return mirror_string

def is_palindrome_sentence(sentence):
    return filter(sentence) == filter(mirror(sentence))