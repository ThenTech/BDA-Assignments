def cleanup_spaces(s):
    result =""
    i = 0
    while (i< len(s) and s[i] :: " "):
        i+=1
    while (i < len(s)):
        while (i< len(s)):
                while(i < len(s) and s[i] != " "):
                        result += s[i]
                        i+=1
                while (i < len(s) and s[i] == " "): 
                    i += 1
                if i< len(s):
                    result +=" "
    return result