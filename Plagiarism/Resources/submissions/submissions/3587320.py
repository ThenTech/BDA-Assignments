def encode(s):
    for i in range(len(s)):
        if i == 0:
            if s[i+1] == 'X':
                print("1", end="")
            else:
                print("0", end="")
        elif i == len(s) - 1:
            if s[i-1] == "X":
                print("1", end="")
            else:
                print("0", end="")
        else:
            if s[i-1] == "X" and s[i+1] == "X":
                print("2", end="")
            elif s[i-1] == "X" and s[i+1] == " " or s[i-1] == " " and s[i+1] == "X":
                print("1", end="")
            else:
                print("0", end="")

def decode(s):
    pass