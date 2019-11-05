def count_words(string):
    verboden_tekens=[1,2,3,4,5,6,7,8,9,0,".","?","!",","]
    for i in range(len(string)):
        if string[i] == verboden_tekens 
        string = string[0:i] + " " +string[i+1:]
        
    lijst = string.split()
    aantal_woorden = len(lijst)
    return aantal_woorden
    pass