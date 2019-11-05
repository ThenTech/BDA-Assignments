# write your code here
def combinaties(n):
    list = ["A","C","G","T"]
    for i in list:
        print(i + combinaties(n-1))

        
        