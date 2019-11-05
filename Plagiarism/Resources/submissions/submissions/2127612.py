eencent=input("Hoeveel centen van 1 heeft u?")
tweecent=input("Hoeveel centen van 2 heeft u?")
vijfcent=input("Hoeveel centen van 5 heeft u?")
tiencent=input("Hoeveel centen van 10 heeft u?")
twintigcent=input("Hoeveel centen van 20 heeft u?")
eencent=int(eencent)
tweecent=int(tweecent)
vijfcent=int(vijfcent)
tiencent=int(tiencent)
twintigcent=int(twintigcent)
eencent=eencent/100
tweecent=tweecent/50
vijfcent=vijfcent/20
tiencent=tiencent/10
twintigcent=twintigcent/5
print("you have ",eencent+tweecent+vijfcent+tiencent+twintigcent, "euro!")