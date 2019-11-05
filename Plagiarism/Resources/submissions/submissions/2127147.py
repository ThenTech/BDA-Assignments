# write your code here
total = int(input("input ur amount"))

aantaltweeeuros = total // 200
print("2-euros: ", int(aantaltweeeuros))
total = total - aantaltweeeuros*200
aantaleeneuros = total // 100
print("1-euros: ", int(aantaleeneuros))
total = float(total - aantaleeneuros*100)
aantalvijftigcents = total // 50
print("50c-euros: ", int(aantalvijftigcents))
total = float(total - aantalvijftigcents*50)
aantaltwintigcents = total // 20
print("20c-euros: ", int(aantaltwintigcents))
total = float(total - aantaltwintigcents*20)
aantaltiencents = total // 10
print("10c-euros: ", int(aantaltiencents))
total = float(total - aantaltiencents*10)
aantalvijfcents = total // 5
print("5c-euros: ", int(aantalvijfcents))
total = float(total - aantalvijfcents*5)
aantaltweecents = total // 2
print("2c-euros: ", int(aantaltweecents))
total = float(total - aantaltweecents*2)
aantaleencents = total // 1
print("1c-euros: ", int(aantaleencents))
total = float(total - aantaleencents*1)