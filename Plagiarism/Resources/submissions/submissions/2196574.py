def cleanup_spaces(s):
    new = s.split()
    string=""
    for i in range(len(new)):
        if i != len(new)-1:
            string += new[i] + " "
        else:
            string += new[i]
    return string
print(cleanup_spaces("    Complex example   String !  "))