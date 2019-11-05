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
    alleopties = subsets(lijstgetallen)
    for optie in alleopties:
        if len(optie) == m:
            index = len(optie)
            for getal in optie:
                index -= 1
                print(optie[index], end=' ')
            print()
    return

n = int(input())
m = int(input())
collectie(n, m)
