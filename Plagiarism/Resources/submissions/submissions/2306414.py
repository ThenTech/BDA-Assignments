def count_words(string):
    alfabet ="azertyuiopqsdfghjklmwxcvbn"
    aantal = 0
    r=0
    for n in string[r:]:
        r+=1
        if n in alfabet:
            if r ==len(string):
               aantal=aantal+1
            else:
               for n in string[r:r+1]: 
                  if n not in alfabet:
                     r+=1
                 
                     
                     aantal = aantal+1
    return aantal             