def encode(s):
    output = ""
    if s == "X" or s == " ":
        return "0"
    for i in range(len(s)):
        if i == 0:
            if s[i + 1] == "X":
                output += "1"
            else:
                output += "0"
        elif i == len(s) - 1:
            if s[i - 1] == "X":
                output += "1"
            else:
                output += "0"
        else:
            count = 0
            if s[i - 1] == "X":
                count += 1
            if s[i + 1] == "X":
                count += 1
            output += str(count)
    return output


def decode(s, n):
    pass