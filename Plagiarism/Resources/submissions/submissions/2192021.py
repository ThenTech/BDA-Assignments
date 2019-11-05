def count_words(s):
    letter_list = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    new_string = ''
    for i in s:
        if i in letter_list:
            new_string += i
        else:
            new_string += ' '
    return len(new_string.split())