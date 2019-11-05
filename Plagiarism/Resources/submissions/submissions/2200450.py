def remove_punctuation(string):
    new_string=""
    verboden_tekens1 = ["0","1","2","3","4","5","6","7","8","9"]
    verboden_tekens2 = [",", "!", ".", ":","?"]
    for i in range(0 , len(string)):
        letter = string[i]
        if letter not in verboden_tekens1:
            new_string = new_string + letter
        elif letter in verboden_tekens2:
            new_string = new_string + " "
    return new_string

lijn = input("Geef een random string op.")
lijst = remove_punctuation(lijn).split()
for i in range (0,len(lijst)):
    woord = lijst[i]
    uitkomst = len(woord)
    print(woord, uitkomst)