def subsets(lijst):
        for item in subsethelper(lijst, []):
            for waarde in item:
                print(waarde, end=" ")
            print()


def subsethelper(lijst, huidige):
    if len(lijst) == 0:
        return [huidige]
    else:
        begin = lijst[0]
        rest = lijst[1:]
        zonder = subsethelper(rest, huidige)
        met = subsethelper(rest, huidige + [begin])
        return zonder + met
ingave = []
for item in input().split():
    ingave.append(int(item))
subsets(ingave)

        