inp = int(input("x?: "))
result = 0
for i in range(1, inp+1):
    temp_res= 0
    for j in range(1, i + 1):
        temp_res += j
    result += temp_res

print(result)