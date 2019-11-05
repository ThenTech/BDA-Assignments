def convert(number):
    x = 0
    counter = 0
    if number != "":
        counter += 1
        convert(number[:len(number)-1])
    x += int(number)*10*counter
    counter -= 1