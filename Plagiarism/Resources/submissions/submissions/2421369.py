def functie(n, result):
    if n < amount:
        for i in range(2):
            if i == 1:
                result += string[n] + " "
            functie(n+1, result)


string = input().split(" ")
amount = len(string)
if string != "":
    functie(0, "")
