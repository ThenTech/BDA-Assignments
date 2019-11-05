import string as string_class


def count_words(string):
    punct = string_class.punctuation
    letters = string_class.ascii_letters
    new_string = ""
    for word in string:
        for letter in word:
            if letter in punct or letter == " ":
                new_string += " "
            if letter in letters:
                new_string += letter

    final_string = new_string.split()
    count = 0
    for i in final_string:
        count += 1
    return count