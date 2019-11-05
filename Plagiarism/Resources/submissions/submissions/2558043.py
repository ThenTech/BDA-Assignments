# write your code here
# stap 1: recursie vinden
    # lijst met elementen => subsets maken: we beginnen met 1 en zetten alle mogenlijke substets met de andere erachter
def subset(l): # niet krachtig genoeg voor recursie
    subset_helper(l,[])
def subset_helper(l,r): # de recursieve functie, met l de lijst en r het al gekende resutlaat
    #basisgeval = als lijst leeg is => print het resultaat
    if len(l)==0:
        for j in r:
            print(j,end=" ")
        print()
    else:
        # telkens kiezen of het 1ste element erin zit of niet(beide doen, en beide met recursie voor het acthervolgende)
        # =>
        eerste = l[0]
        rest = l[1:]
        #niet toevoegen
        subset_helper(rest,r)
        #wel
        subset_helper(rest,r+[eerste])

lijst = input()
lijst = lijst.split()
subset(lijst)