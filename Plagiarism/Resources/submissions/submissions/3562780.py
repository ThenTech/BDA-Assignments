een_cent = int(input("munten van 1 cent: "))
twee_cent = int(input("munten van 2 cent: "))*2
vijf_cent = int(input("munten van 5 cent: "))*5
tien_cent = int(input("munten van 10 cent: "))*10
twintig_cent = int(input("munten van 20 cent: "))*20

totaal = een_cent + twee_cent + vijf_cent + tien_cent + twintig_cent


honderdtallen = totaal % 10
tientallen = (totaal//10)%10
eenheden = (totaal//100)

print("You have ", eenheden, ".", tientallen, honderdtallen, " euro!", sep="")