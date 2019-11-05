string11 = input('Geef een woord in')
string22 = input('geef tweede woord')
aantal_letters1=""
aantal_letters2=""

alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

string1=""
string2=""
for x in string11:
    if x != " ":
        string1 = string1 + x
for x in string22:
    if x != " ":
        string2 = string2 + x

string1_lijst = list(string1)
string2_lijst = list(string2)

if len(string1_lijst) == len(string2_lijst):
    for el in alfabet:
        teller1 = 0
        teller2=0
        for waarde in string1_lijst:
            if el == waarde:
                teller1 = teller1 + 1
        aantal_letters1 = aantal_letters1 + str(teller1)
        for waarde in string2_lijst:
            if el == waarde:
                teller2 = teller2 + 1
        aantal_letters2 = aantal_letters2 + str(teller2)
    if aantal_letters1 == aantal_letters2:
        print(string11, "and", string22, "are anagrams")
    else:
        print(string11, "and", string22, "are not anagrams")

else:
    print(string11, "and", string22, "are not anagrams")