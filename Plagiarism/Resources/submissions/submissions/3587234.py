def cleanup_spaces(s):
    letterPassed = False
    punctuationPassed = False
    tempString = ""
    
    for i in s:
        if 'a' <= i.lower() <= 'z':
            letterPassed = True
            tempString += i
            
        elif i != " " and not('a' <= i.lower() <= 'z'):
            punctuationPassed = True
            tempString += i
            
        elif i == " " and (letterPassed or punctuationPassed):
            tempString += i
            letterPassed = False
            punctuationPassed = False


            
    return tempString
        