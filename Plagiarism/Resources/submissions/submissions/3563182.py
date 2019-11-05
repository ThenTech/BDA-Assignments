def count_words(string):
    non_initeresting_ch = " !,:;?.=+()@/0123456789"
    if string[len(string) - 1] not in non_initeresting_ch:
        string += " "
    count = 0
    if len(string) == 0:
        return 0
    for i in range(len(string)-1):
        if string[i] in non_initeresting_ch and string[i+1] not in non_initeresting_ch:
            count += 1
    if string[len(string) - 2] not in non_initeresting_ch:
        count += 1
    return count