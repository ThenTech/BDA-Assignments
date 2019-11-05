inp = input()

def to_words(string):
    ab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prntstr = ''
    last_letter = False
    for x in string:
        if x in ab:
            prntstr += x
            last_letter = True
        elif (x not in ab) and (last_letter):
            print(prntstr, len(prntstr))
            prntstr = ''
            last_letter = False
            
to_words(inp)