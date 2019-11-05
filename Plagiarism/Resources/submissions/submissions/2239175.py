def woordteller(string):
    count = 0
    teller = 0
    inwoord = False
    for i in string:
        if i == string[-1]:
            slice = string[teller - (count):teller+1]
            print(slice, count)
        if "a" <= i <= "z" or "A" <= i <= "Z":
            inwoord = True
            count = count+1
            teller = teller+1
        else:
            if inwoord:
                slice = string[teller-(count):teller]
                print(slice, count)
                teller = teller + 1
                count = 0
                inwoord = False

            
                
        
    