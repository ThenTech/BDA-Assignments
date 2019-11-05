def cleanup_spaces(s):
    letterPassed = False
    punctuationPassed = False
    tempString = ""
    
    for i in s:
        if 'a' <= i.lower() <= 'z':
            letterPassed = True
            tempString += i
            
        elif i != " " and not('a' <= i.lower() <= 'z'):
            PunctuationPassed = True
            tempString += i
            
        elif i == " " and (letterPassed or PunctuationPassed):
            tempString += i
            letterPassed = False
            PunctuationPassed = False


            
    return tempString
        