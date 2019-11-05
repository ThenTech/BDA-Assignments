totaal_eurocent = int(input("Aantal opgegeven eurocent is: "))

twee_euros = totaal_eurocent // 200
rest = totaal_eurocent - 200*twee_euros
een_euros = rest // 100
rest = rest - 100*een_euros
vijftig_cent = rest // 50
rest = rest - 50*vijftig_cent
twintig_cent = rest // 20
rest = rest - 20*twintig_cent
tien_cent = rest // 10
rest = rest - 10*tien_cent
vijf_cent = rest // 5
rest = rest - 5*vijf_cent
twee_cent = rest // 2
rest = rest - 2*twee_cent
een_cent = rest

print("2-euros:", twee_euros)
print("1-euros:", een_euros)
print("50c-euros:", vijftig_cent)
print("20c-euros:", twintig_cent)
print("10c-euros:", tien_cent)
print("5c-euros:", vijf_cent)
print("2c-euros:", twee_cent)
print("1c-euros:", een_cent)
