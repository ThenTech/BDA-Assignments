import random as r

List = []


def quick_sort(l):
    
    if len(l) <= 1:
        return l
    global List
    if len(List) == 0:
        List = l

    Result = []
    Wait = []
    Numb = []
    
    rnum = r.randrange(0, len(List))

    for i in l:
    
        if i < List[rnum]:
            Result.append(i)
        elif i > List[rnum]:
            Wait.append(i)
        elif i == List[rnum]:
            Numb.append(i)
    for i in Numb:
        Result.append(i)
    for i in Wait:
        Result.append(i)
        
    List.remove(List[rnum])
    if (len(List) > 0):
        quick_sort(Result)
    else:
        return Result