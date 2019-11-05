def count_words(string):
    teller = 1
    woorden = string.split()
    alfabet = 'qwertyuiopasdfghjklzxcvbnm'
    for woord in woorden:
        for letter in woord:
            if letter not in alfabet:
                teller += 1
    return teller
print(count_words("five 6 seven,eight!nine"))