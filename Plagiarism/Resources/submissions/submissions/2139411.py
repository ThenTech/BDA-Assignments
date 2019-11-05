woord = input('Geef je woord in: ')
alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
woordlijst = list(woord)
teller = 0
for x in alfabet:
    for y in woordlijst:
        if x == y:
            teller = teller + 1
    print (x,': ', teller,sep='')
    teller = 0