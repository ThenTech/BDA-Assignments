def remove_punctuation(string):
    new_string=""
    verboden_tekens = [",", "!", ".", ":"]
    for i in range(0 , len(string)):
        letter = string[i]
        if letter not in verboden_tekens:
            new_string = new_string + letter
    return new_string

lijn = input("Geef een random string op.")
lijst = remove_punctuation(lijn).split()
for i in range (0,len(lijst)):
    woord = lijst[i]
    uitkomst = len(woord)
    print(woord, uitkomst)