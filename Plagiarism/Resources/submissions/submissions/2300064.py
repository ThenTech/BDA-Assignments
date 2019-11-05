def is_unique(l):
    unique = True
    for i in range(0, len(l)):
        for j in l[i+1:]:
            if l[i] != j:
                continue
            else:
                unique = False
                break
        if not unique:
            break
    return unique


def is_magic_square(matrix):
    all_numbers = []
    for i in matrix:
        all_numbers += i

    if is_unique(all_numbers):
        oldsum = 0
        for i in range(0, len(matrix)):
            sum = 0
            for j in range(0, len(matrix[i])):
                sum += int(matrix[i][j])
            if i == 0:
                oldsum = sum
            else:
                if oldsum == sum:
                    continue
                else:
                    return False

        for k in range(0, len(matrix)):
            sum = 0
            for l in range(0, len(matrix[k])):
                sum += int(matrix[l][k])
            if l == 0:
                oldsum = sum
            else:
                if oldsum == sum:
                    continue
                else:
                    return False
        sum = 0
        for m in range(0, len(matrix)):
            sum += matrix[m][m]
        if oldsum != sum:
            return False

        sum = 0
        for i in range(len(matrix)):
            sum += matrix[len(matrix) - i - 1][len(matrix) - i - 1]
        if oldsum != sum:
            return False
        return True
    else:
        return False

print(is_magic_square([[8, 1, 6], [3, 5, 7], [4, 9, 2]]))
