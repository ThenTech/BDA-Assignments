def cleanup_spaces(s):

    split_string = ""
    answer = ""

    for i in range(len(s)):
        if s[i] != " ":
            split_string += s[i]
        if s[i] == " " and i + 1 < len(s):
            if s[i + 1] == " ":
                split_string += ""
            if s[i + 1] != " ":
                split_string += s[i]
        if s[len(s) - 1] == " ":
            split_string += ""

    if len(split_string) == 0:
        return split_string
    if split_string[0] == " ":
        answer = split_string[1:]
        return answer
    else:
        return split_string