# write your code here
total = int(input("input ur amount"))

aantaltweeeuros = total // 200
print("2-euros: " + str(aantaltweeeuros))
total = total - aantaltweeeuros*200
aantaleeneuros = total // 100
print("1-euros: " + str(aantaleeneuros))
total = float(total - aantaleeneuros*100)
aantalvijftigcents = total // 50
print("50c-euros: " + str(aantalvijftigcents))
total = float(total - aantalvijftigcents*50)
aantaltwintigcents = total // 20
print("20c-euros: " + str(aantaltwintigcents))
total = float(total - aantaltwintigcents*20)
aantaltiencents = total // 10
print("10c-euros: " + str(aantaltiencents))
total = float(total - aantaltiencents*10)
aantalvijfcents = total // 5
print("5c-euros: " + str(aantalvijfcents))
total = float(total - aantalvijfcents*5)
aantaltweecents = total // 2
print("2c-euros: " + str(aantaltweecents))
total = float(total - aantaltweecents*2)
aantaleencents = total // 1
print("1c-euros: " + str(aantaleencents))
total = float(total - aantaleencents*1)