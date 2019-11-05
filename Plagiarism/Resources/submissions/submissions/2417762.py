# write your code here
list = input()
list =list.split()
vorige = ""
def checker(list,vorige):
    if len(list) ==0:
        return 
    else:
        new_list = list[1:]
        new_vorige = vorige + " " +list[0]
        checker(new_list,new_vorige)
        return(new_vorige)
        checker(new_list,vorige)
checker(list,vorige)