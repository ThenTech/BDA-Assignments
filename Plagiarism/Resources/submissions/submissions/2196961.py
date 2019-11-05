def count_words(string):
    print(string)
    lijst = string.split()
    print(lijst)
    verboden_tekens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,".","?","!",","]
    for i in range(len(string)):
        if string[i] in verboden_tekens:
            string = string[0:i] + " " + string[i+1]
    lijst = string.split()
    print(lijst)
    return len(lijst)
count_words("five 6 seven,eight!nine")