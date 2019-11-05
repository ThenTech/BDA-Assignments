# write your code here
list = ["A","C","G","T"]
def combinaties(n):
    for i in range(n):
        for j in range(n):
            print(list[i] + list[j])
        