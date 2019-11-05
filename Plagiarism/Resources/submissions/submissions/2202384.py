def cleanup_spaces(s):
    string_without_punct = ""
    end = 0
    start = 0
    counter = 0
    for letter in s:
        if letter != " ":
            string_without_punct = string_without_punct + letter
            end = end + 1
            counter = counter + 1
        else:
            if start != end:
                string_without_punct = string_without_punct + " "
                start = end
            else:
                while s[counter] == " ":
                    string_without_punct = string_without_punct + ""
                    counter = counter + 1
    if string_without_punct[len(string_without_punct) - 1] == " ":
        string_without_punct = string_without_punct[:len(string_without_punct)-1]
    return(string_without_punct)