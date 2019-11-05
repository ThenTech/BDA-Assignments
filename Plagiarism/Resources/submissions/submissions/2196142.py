def convert_to_uppercase(s):
    new_string = ''
    list_a = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i in list_a:
            new_string += chr((ord(i)-32))
        else:
            new_string += i