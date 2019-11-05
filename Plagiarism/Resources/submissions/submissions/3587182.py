def cleanup_spaces(s):
    letterPassed = False
    tempString = ""
    
    for i in s:
        if i != " " and letterPassed = True:
            tempString += i
            letterPassed = False
        else:
            letterPassed = True
        