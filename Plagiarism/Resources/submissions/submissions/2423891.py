def subsets(n, m, string):
    if string.count(" ") < m:
        for i in range(m):
            if n-i > 0:
                result = string
                result += str(n-i) + " "
                subsets(n-i-1, m, result)
                if result.count(" ") == m:
                    print(result)


subsets(int(input()), int(input()), "")