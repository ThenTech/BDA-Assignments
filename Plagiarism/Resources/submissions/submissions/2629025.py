def encode(s):
    listy = []
    listy_num = []
    for i in s:
        listy.append(i)
        listy_num.append(0)
    for i in range(len(listy)):
        if i == 0 and s[i] == "X":
            listy_num[i + 1] += 1
        elif i == len(listy)-1 and s[i] == "X":
            listy_num[i - 1] += 1
        elif i > 0 and i < len(listy)-1:
            if listy[i] == " ":
                continue
            else:
                listy_num[i-1] += 1
                listy_num[i+1] += 1
    return listy_num

def make_empty_list(s):
    listy = []
    listy_num = []
    for i in s:
        listy_num.append(i)
        listy.append("")
    return (listy_num, listy)

# def decode(s):
#     for i in [" ", "X"]:
#         listy_num, listy = make_empty_list(s)
#         listy[0] = i
#         for i in range(1, len(listy_num[1:len(listy_num)])):
#             if listy_num[i-1] == "2":
#                 listy[i] = "X"
#                 listy[i] = "X"
#             elif listy_num[i-1] == "1" and listy[i-1] == " ":
#                 listy[i] = "X"
#             else:
#                 listy[i] = " "