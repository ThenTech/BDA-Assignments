def cleanup_spaces(s):
    letterPassed = False
    tempString = ""
    
    for i in s:
        if 'a' <= i.lower() <= 'z':
            letterPassed = True
            
        elif i != " " and letterPassed:
            tempString += i
            letterPassed = False
        else:
            letterPassed = True
            tempString += i
            
    return tempString
        