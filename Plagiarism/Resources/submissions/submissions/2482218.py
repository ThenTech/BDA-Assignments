string = str(input())


def cleanup_spaces(string):
    result = ""
    i = 0

    while i < len(string) and string[i] == " ":
        i += 1

    while i < len(string):

        while i < len(string) and string[i] != " ":
            i += 1
            result += string[i]

        while i < len(string) and string[i] == " ":
            i += 1
            
        if i < len(string):
            result += string[i]

    return result


print(cleanup_spaces(string))