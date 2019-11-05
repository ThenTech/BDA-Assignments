TeBetalen = 589
TweeEuro = 589 // 200
TE = 589 - (TweeEuro * 200)
EenEuro = TE // 100
EE = TE - (EenEuro * 100)
HalveEuro = EE // 50
HE = EE - (HalveEuro * 50)
Twintigcent = HE // 20
TC = HE - (Twintigcent * 20)
Tiencent = TC // 10
TiC = TC - (Tiencent * 10)
Vijfcent = TiC // 5
VC = TiC - (Vijfcent * 5)
Tweecent = VC // 2
TC = VC - (Tweecent * 2)
Eencent = TC // 1 
EC = TC - (Eencent * 1)
print("2-euros: ", TweeEuro)
print("1-euros: ", EenEuro)
print("50c-euros : ", HalveEuro)
print("20c-euros : ", Twintigcent)
print("10c-euros : ", Tiencent)
print("5c-euros : ", Vijfcent)
print("2c-euros : ", Tweecent)
print("1c-euros : ", Eencent)