cent = input("hoeveel cent")
cent = int(cent)

for value in (200,100,50,20,10,5,2,1):

    euros = cent/value
    euros = int(euros)

    cent -= (value*euros)
    
    if value == 200:
        print ("2-euros:",euros)
    if value == 100:
        print ("1-euros:",euros)
    if value == 50:
        print ("50c-euros:",euros)
    if value == 20:
        print ("20c-euros:",euros)
    if value == 10:
        print ("10c-euros:",euros)
    if value == 5:
        print ("5c-euros:",euros)
    if value == 2:
        print ("2c-euros:",euros)
    if value == 1:
        print ("1c-euros:",euros)
    
