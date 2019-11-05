def create_sequence(string, index, length):
        for i in range(index,index+length):
            k = i % len(string)
            return string[k]
pass