woord1 = str(input("Geef woord 1: "))
woord2 = str(input("Geef woord 2: "))
if sorted(woord1)==sorted(woord2):
    print(woord1,"and",woord2,"are anagrams")
else:
    print(woord1,"and",woord2,"are not anagrams")