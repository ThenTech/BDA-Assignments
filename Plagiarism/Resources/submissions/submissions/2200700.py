def convert_to_uppercase(s):
    nieuw = ""
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    down = "abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i in up:
            nieuw += i
        else:
            teller = 0
            for j in down:
                if i == j:
                    nieuw += up[teller]
                else:
                    teller +=1
    return nieuw