# zet input ook om naar lijst!!
l = input()  # elementen waar we nog uit moeten kiezen eig
l = l.split()


# String eerst omzetten naar een lijst!!


def subset(l):
    find_subsets(l, [])

def find_subsets(l, result):  # beide zijn lijsten, result om bij te houden wat je tot nu toe al hebt
    if len(l) == 0:  # geen elementen meer om te kiezen
        print()
        for combination in result:
            for char in combination:
                print(combination, "", end = "")

    else:
        eerste = l[0]
        rest = l[1:]

        # eerste char niet toevoegen
        find_subsets(rest, result)

        # eerste char wel toevoegen
        find_subsets(rest, result + [eerste])


subset(l)