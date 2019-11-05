def subsets(list):
    return subset_helper(list, [])
        
def subset_helper(s, huidige):
    if len(s) == 0:
        return [huidige]
    else:
        begin = s[0]
        rest = s[1:]
        zonder = subset_helper(rest, huidige)
        met = subset_helper(rest, huidige + [begin])
        return zonder + met

def lijstmaken(getal):
    lijst = []
    huidig = 0
    for x in range(getal):
        huidig += 1
        lijst.append(huidig)
    return lijst
 def collectie(n, m):
     lijstgetallen = lijstmaken(n)
     alleopties =subsets(lijstgetallen)
     for optie in alleopties:
         if len(optie) == m:
             for getal in optie:
                 print(getal,end=' ')
        print()
        
n = input()
m = input()
collectie(n, m)
        