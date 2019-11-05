eencent = int(input("Geef aantal eencenten: "))
tweecent = int(input(""))
vijfcent = int(input(""))
tiencent = int(input(""))
twintigcent = int(input(""))

som = 1*eencent + 2*tweecent + 5*vijfcent + 10*tiencent + 20*twintigcent

euros = som // 100
centen = som - 100*euros
tiencenten = centen //10
eencenten = centen - 10*tiencenten

print("You have ", euros, ".", tiencenten, eencenten, " euro!", sep="")