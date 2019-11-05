def string(input):
    current = ""
    for i in input:
        if not (97 <= ord(i) <= 122 or 65 <= ord(i) <= 90) and len(current) == 0:
            continue
        elif not (97 <= ord(i) <= 122 or 65 <= ord(i) <= 90):
            print(current, len(current))
            current = ""
        else:
            current += i
    if len(current) != 0:
        print(current, len(current))

string(input("Give an input: "))