def count_words(string):
    numbers = "0123456789"
    index = 0
    for char in string:
        if (ord(char) < 65 or ord(char) > 90) and (ord(char) < 97 or ord(char) > 122):
            if index != 0:
                string = string[:index] + " " + string[index + 1:]
            else:
                string = string[index + 1:]
        index += 1

    list_words = string.split()
    return len(list_words)
