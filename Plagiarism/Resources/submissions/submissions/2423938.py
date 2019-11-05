def subsets(n, m, string):
    if string.count(" ") < m:
        for i in range(m):
            if n-i > 0:
                result = string
                result += str(n-i) + " "
                subsets(n-i-1, m, result)
                if result.count(" ") == m:
                    print(result)


n_input = int(input())
m_input = int(input())

if m_input != 0:
    subsets(n_input, m_input, "")
else:
    print()