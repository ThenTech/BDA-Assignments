totaal = int(input("Aantal eurocent"))
twee_euro = totaal//200
totaal_1 = totaal - twee_euro*200
een_euro = totaal_1//100
totaal_2 = totaal_1 - een_euro*100
vijftig_cent = totaal_2//50
totaal_3 = totaal_2 - vijftig_cent*50
twintig_cent = totaal_3//20
totaal_4 = totaal_3 - twintig_cent*20
tien_cent = totaal_4//10
totaal_5 = totaal_4 - tien_cent*10
vijf_cent = totaal_5//5
totaal_6 = totaal_5 - vijf_cent*5
twee_cent = totaal_6//2
totaal_7 = totaal_6 - twee_cent*2
een_cent = totaal_7//1
totaal_8 = totaal_7 - een_cent*1
print("2-euros:", twee_euro)
print("1-euros:", een_euro)
print("50c-euros:", vijftig_cent)
print("20c-euros:", twintig_cent)
print("10c-euros:", tien_cent)
print("5c-euros:", vijf_cent)
print("2c-euros:", twee_cent)
print("1c-euros:", een_cent)
