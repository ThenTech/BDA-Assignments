def in_range(r, nr):
    return 0 <= nr < r


def encode_helper(s):
    output = ""

    for i in range(len(s)):
        nr = 0
        if in_range(len(s), i-1) and s[i-1] == "X":
            nr += 1
        if in_range(len(s), i+1) and s[i+1] == "X":
            nr += 1
        output += str(nr)

    return output


def encode(s):
    print(encode_helper(s))


def decode_helper(s, r, output):
    if len(r) == len(s):
        if encode_helper(r) == s:
            output.append(r)
    else:
        decode_helper(s, r + " ", output)
        decode_helper(s, r + "X", output)

    return output


def decode(s):
    output = decode_helper(s, "", [])

    for i in output:
        print(i)
