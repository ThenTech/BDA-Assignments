def count_words(string):
    numbers = "0123456789"
    index = 0
    for char in string:

        if (ord(char) < 65 or ord(char) > 90) and (ord(char) < 97 or ord(char) > 122):
            if index != 0:
                new_string = string[:index] + " " + string[index + 1:]
            else:
                new_string = string[index + 1:]
        index += 1

    print(new_string)
    list_words = new_string.split()
    return len(list_words)