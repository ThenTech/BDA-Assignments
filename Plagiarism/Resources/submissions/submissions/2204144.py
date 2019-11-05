def count_words(string):
    inword = False
    count = 0
    for i in string:
        if "a" <= i <= "z" or "A" <= i <= "Z":
            inword = True
        else:
            if inword:
                count += 1
            inword = False
    if "a" <= i <= "z" or "A" <= i <= "Z":
        count += 1
      
    return count
print(count_words("one two"))