def convert_to_uppercase(string):
    nieuwe_string = ""
    for el in string:
        alfabet ="azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN"
        if not el in alfabet:
            nieuwe_string = nieuwe_string + el
        elif 'A' <= el <= 'Z':
            nieuwe_string = nieuwe_string + el
        else:
            el = chr(int(ord(el))-32)
            nieuwe_string = nieuwe_string + el
    return nieuwe_string