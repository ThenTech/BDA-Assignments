def collections(n, m, list):
    if len(list) == m:
        output = ""
        for i in range(len(list)):
            output += str(list[i])
            if i != len(list) - 1:
                output += " "
        print(output)
    else:
        for i in range(n):
            collections(n - i - 1, m, list + [n - i])


n = int(input("n = ?\n"))
m = int(input("m = ?\n"))
collections(n, m, [])
