def count_words(string):
    word=""
    count=0
    for i in string:
        if i in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN":
            word+=i
        elif i not in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN":
            word+=" "
    woord=word.split()
    for i in woord:
        count+=1
    return count