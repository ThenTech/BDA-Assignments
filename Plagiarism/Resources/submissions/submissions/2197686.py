def cleanup_spaces(string):
    space_count = 0
    cleaned_string = ""
    index = 0
    for char in string:
        if char == " ":
            space_count += 1
        else:
            if space_count > 1:
                cleaned_string += string[index-1: index+1]
            elif space_count == 1:
                cleaned_string += " " + string[index]
            else:
                cleaned_string += string[index]
            space_count = 0
        index += 1

    if cleaned_string[0] == " ":
        cleaned_string = cleaned_string[1:]
        
    return cleaned_string