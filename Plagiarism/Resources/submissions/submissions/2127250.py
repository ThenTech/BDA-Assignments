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
TC : VC - (Tweecent * 2)
Eencent = TC // 1 
EC = TC - (Eencent * 1)
print("Te betalen munten van 2 euro: ", TweeEuro)
print("Te betalen munten van 1 euro: ", EenEuro)
print("Te betalen munten van een halve euro : ", HalveEuro)
print("Te betalen munten van twintig cent: ", Twintigcent)
print("Te betalen munten van tien cent: ", Tiencent)
print("Te betalen munten van vijf cent: ", Vijfcent)
print("Te betalen munten van twee cent: ", Tweecent)
print("Te betalen munten van een cent: ", Eencent)