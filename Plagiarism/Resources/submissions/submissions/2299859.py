def is_magic_square(matrix):
    if len(matrix) <= 1:
       return True
    if len(matrix[0])==len(matrix):
        l =[]

            for i in range (0, len(matrix[0])):
                l += matrix [i]
            
            for m in range (0,len(l)-1):
                for k in range (m+1, len(l)):
                    if l[k] == l[m]:
                        return False
                if False:
                     break
                if m == len(l)-2:
                    for i in range (0, len(matrix[0])):
                        m2 = 0
                        m3 = 0
                        m4 = 0
                        m5 = 0
                        for j in range (0, len(matrix[0])):
                            m2 += matrix [i][j]
                            m3 += matrix [j][j]
                            m4 += matrix [j][i]
                            m5 += matrix [len(matrix[0])-1-j][len(matrix[0])-1-j]
                        if m2 != m3 or m2 != m4 or m2 != m5:
                            return False
                        if i == len(matrix[0])-1:
                            return True
    else:
        return False
