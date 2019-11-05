def convert_to_uppercase(string):
    sans_lower = ""
    for i in string:
        if "a" <= i <= "z":
            result = chr(ord(i) - ord("a") + ord("A"))
            sans_lower += result
        else:
            sans_lower += i
    return sans_lower