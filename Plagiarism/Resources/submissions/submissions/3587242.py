def cleanup_spaces(s):
    letterPassed = False
    punctuationPassed = False
    tempString = ""
    
    for i in range(len(s)):
        if 'a' <= s[i].lower() <= 'z':
            letterPassed = True
            tempString += s[i]
            
        elif s[i] != " " and not('a' <= s[i].lower() <= 'z'):
            punctuationPassed = True
            tempString += s[i]
            
        elif s[i] == " " and (letterPassed or punctuationPassed) and (i+1) != " ":
            tempString += s[i]
            letterPassed = False
            punctuationPassed = False


            
    return tempString
        