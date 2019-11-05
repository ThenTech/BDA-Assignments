def cleanup_spaces(s):
    letterPassed = False
    tempString = ""
    
    for i in s:
        if i != " ":
            letterPassed = True
            tempString += i
            
        elif i == " " and letterPassed:
            tempString += i
            letterPassed = False


            
    return tempString
        