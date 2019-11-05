kleinalfabet = "abcdefghijklmnopqrstuvwxyz"
grootalfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert_to_uppercase(string):
    woord = ''
    for letter in string:
        if letter in kleinalfabet:
            teller = -1
            for x in kleinalfabet:
                teller += 1
                if x == letter:
                    break
            woord += grootalfabet[teller]
        else:
            woord += letter
            continue
    return woord
print(convert_to_uppercase("steve is snel"))