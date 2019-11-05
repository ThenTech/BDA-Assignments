# write your code here
# write your code here
def combinaties(n):
    list = ["A","B","C","D"]
    if n ==0:
        for i in list:
            print(i)

    for i in list:
        print(i + combinaties(n-1))
combinaties(2)