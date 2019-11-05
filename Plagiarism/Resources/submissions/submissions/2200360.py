def cleanup_spaces(s):
    teller = 0
    niet = ''',?;.:/"<>[]^!'“”’ '''
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nieuw = ""
    for i in s:
        if teller == len(s)-1:
            if i == " ":
                continue
            else:
                nieuw += i
        elif i == " ":
            if s[teller+1] == " ":
                if s[teller-1] in alfabet:
                    nieuw += " "
                    teller += 1
                else:
                    teller += 1
            elif s[teller-1] in alfabet:
                nieuw += " "
                teller +=1
            else:
                teller += 1
        else:
            nieuw += i
            teller += 1
    return nieuw
print(cleanup_spaces("   A man,  a plan,   but not a canal  :  Panama.  "))