def convert_to_uppercase(s):
    uppercased_string = ""
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            uppercased_string += chr(ord("A") + ord(s[i]) - ord("a"))
        else:
            uppercased_string += s[i]
    return uppercased_string