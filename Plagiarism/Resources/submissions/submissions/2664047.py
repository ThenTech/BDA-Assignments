def cleanup_spaces(s):
    result = ""
    i = 0

    # skip any initial whitespace
    while (i < len(s) and s[i] == ' '):
        i += 1

    # process pairs of words, whitespace
    while (i < len(s)):
        # read word
        while (i < len(s) and s[i] != ' '):
            result += s[i]
            i += 1

        # skip all whitespace after word
        while (i < len(s) and s[i] == ' '):
            i += 1

        # if something after all whitespace,
        # then keep one whitespace
        if (i < len(s)):
            result += ' '

    return result
