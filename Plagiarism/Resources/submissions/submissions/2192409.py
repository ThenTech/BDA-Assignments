inp = input()

def to_words(string):
    ab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prntstr = ''
    for x in string:
        if x in ab:
            prntstr += x
        elif x not in ab:
            print(prntstr, len(prntstr))
            prntstr = ''
            
to_words(inp)