def convert(number):
    if len(number)>1:
        return int(number[0]) + convert(number[1:])
    else:
        return(int(number[0]))