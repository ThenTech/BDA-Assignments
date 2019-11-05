def cleanup_spaces(s):
    while "  " in s:
        for i in range(len(s)):
            if s[i] == " " and s[i + 1] == " ":
                s = s[:i] + s[i + 1:]
                break
    if s == " " or s == "":
        return ""

    if s[0] == " ":
        s = s[1:]
    if s[-1] == " ":
        s = s[: len(s) - 1]
    return s