def cleanup_spaces(s):
    letterPassed = False
    tempString = ""
    
    for i in s:
        if 'a' <= i.lower() <= 'z':
            letterPassed = True
            tempString += i
            
        elif i != " ":
            letterPassed = False
            tempString += i
            
        elif i == " " and letterPassed:
            tempString += i
            letterPassed = False


            
    return tempString
        