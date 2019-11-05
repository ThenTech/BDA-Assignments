string = ""

def convert_to_uppercase(string):
    for c in string:
        string = chr(ord(c) - 32)
        print(string, end="")

convert_to_uppercase(string)