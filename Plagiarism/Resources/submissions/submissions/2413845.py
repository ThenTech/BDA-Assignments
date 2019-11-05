# write your code here
# write your code here
def combinaties(n):
    list = ["A","B","C","D"]
    for i in list:
        print(i + combinaties(n-1))