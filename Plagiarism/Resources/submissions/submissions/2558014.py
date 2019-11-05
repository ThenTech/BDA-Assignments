#zet input ook om naar lijst!!
l = input() # elementen waar we nog uit moeten kiezen eig

def subset(l):
    find_subsets(l, [])

def find_subsets(l, result):    # beide zijn lijsten, result om bij te houden wat je tot nu toe al hebt
    
    if len(l) == 0: #geen elementen meer om te kiezen
        for value in result:
            print(value)

    else:
        
        eerste = l[0]
        rest = result[1:]
        
        #eerste char niet toevoegen
        find_subsets(rest, result)
        
        #eerste char wel toevoegen
        find_subsets(rest, result + [eerste])

subset(l)
