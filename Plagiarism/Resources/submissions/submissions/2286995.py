eurocent = int(input('Geef het aantal eurocent:'))
twee_euros = eurocent // 200
een_euros = eurocent % 200 // 100
vijftigC_euros= eurocent % 500 // 50
twintigC_euros= eurocent % 500 % 50 // 20 
tienC_euros = eurocent % 500 % 50 % 20 // 10
vijfC_euros = eurocent % 500 % 50 % 20 % 10 // 5
tweeC_euros = eurocent % 500 % 50 % 20 % 10 % 5 // 2
eenC_euros = eurocent % 500 % 50 % 20 % 10 % 5 % 2 // 1

print('2-euros: ', twee_euros)
print('1-euros: ', een_euros)
print('50c-euros: ', vijftigC_euros)
print('20c-euros: ', twintigC_euros)
print('10c-euros: ', tienC_euros)
print('5c-euros: ', vijfC_euros)
print('2c-euros: ', tweeC_euros)
print('1c-euros: ', eenC_euros)