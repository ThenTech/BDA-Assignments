def create_sequence(string, index, length):
    #declerations
    ans = ''

    #functions
    for i in range(index, length + index):
        ans += string[i % len(string)]
    return ans