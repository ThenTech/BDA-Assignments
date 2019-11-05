total = int(input("Totaal eurocent: "))
for k in ["2", "1", "50c", "20c", "5c", "2c", "1c"]:
    if k == "2" or k == "1":
        print(k + "-euros:", total // (int(k) * 100))
        total = total % (int(k) * 100)
    elif k == "50c" or k == "20c":
        print(k + "-euros:", total // int(k[0:2]))
        total = total % (int(k[0:2]))
    else:
        print(k + "-euros:", total // int(k[0]))
        total = total % int(k[0])