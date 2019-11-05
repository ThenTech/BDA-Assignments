# write your code here
def combinaties(n):
    list = ["A","C","G","T"]
    for i in range(n):
        for j in range(n):
            print(list[i] + list[j])
        
        