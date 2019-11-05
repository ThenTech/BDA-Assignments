def unique_elements(mx):
    element_list =[]
    for i in range(len(mx)):
        for j in range(len(mx)):
            element_list.append(mx[i][j])
    for i in range(len(element_list)):
        count = 0
        for j in range(len(element_list)):
            if element_list[i] == element_list[j]:
                count += 1
            if count == 2:
                return False
    return True

def check_sum(mx):
    som = 0
    for j in range(len(mx)):
        som += mx[0][j]
    return som
        

def sommen(mx):
    checksum = check_sum(mx)
    
    for i in range(len(mx)):
        som1 = 0
        som2 = 0
        for j in range(len(mx)):
            som1 += mx[i][j]
            som2 += mx[j][i]
        if som1 != checksum or som2 != checksum:
            return False
            
    som3 = 0
    som4 = 0
    for i in range(len(mx)):
        som3 += mx[i][i]
        som4 += mx[len(mx) - i - 1][len(mx) -i - 1]
    if som3 != checksum or som4 != checksum:
        return False
    return True
        
        
def is_magic_square(matrix):
    if len(matrix) % 2 == 0:
        return False
    if unique_elements(matrix) and sommen(matrix):
        return True
    return False