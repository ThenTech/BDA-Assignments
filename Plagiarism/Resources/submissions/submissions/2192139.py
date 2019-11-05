alfabet="abcdefghijklmnopqrstuvwxyz"
def count_word ( string ) :
    x=0
    gespl = string.split()
    for i in gespl:
        if i[0] in alfabet:
            x=x+1
    print(x)
count_word(word)