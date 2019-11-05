def substring(string, first, amount):
    """Returns the substring (starting from first with a length of amount) from the given string"""
    total = 0
    count = 0
    word = ""

    for letter in string:
        total += 1
        if total > first and count < amount:
            word += letter
            count += 1
    return word



def find_pos(word_to_find, the_string):
    position = 0
    count = 0

    for letter in the_string:
        if letter == word_to_find[0]:

            for x in range(len(word_to_find)):
                if word_to_find[x] == the_string[position + x]:
                    count +=1
                if count == len(word_to_find):
                    return position
        
        position += 1

def in_string(word_to_find, the_string):
    position = 0
    count = 0

    for letter in the_string:
        if letter == word_to_find[0]:

            for x in range(len(word_to_find)):
                if word_to_find[x] == the_string[position + x]:
                    count += 1
                else:
                    return False
                if count == len(word_to_find):
                    return True
        
        position += 1
    return False