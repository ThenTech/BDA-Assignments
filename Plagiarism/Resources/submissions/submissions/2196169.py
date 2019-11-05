def cleanup_spaces(s):
    lenght = len(s)
    lastletter = ""
    output = ""
    #print("len: ", lenght)          #impovised debug-log

    for i in range(0,lenght):       #elke plaats in de string afgaan
        #print("teller(i): ", i)     #improvised debug-log
        newletter = s[i]            #newletter krijgt value van huidige plaats
        #print(newletter)            #improvised debug-log

        if newletter == " ":
            if lastletter != " " and lastletter != "":
                output += s[i]
                #print("LL != space")    #improvised debug-log
            else:
                print("continue")
                continue
        else:
            output += s[i]
            #print("NL != space")    #impovide debug-log

        lastletter = newletter
    return output