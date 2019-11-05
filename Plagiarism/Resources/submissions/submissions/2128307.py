bedrag=int(input("Geef hier het bedrag in."))
euro_2=bedrag//200
euro_1=(bedrag-euro_2*200)//100
cent_50=(bedrag-euro_2*200-euro_1*100)//50
cent_20=(bedrag-euro_2*200-euro_1*100-cent_50*50)//20
cent_10=(bedrag-euro_2*200-euro_1*100-cent_50*50-cent_20*20)//10
cent_5=(bedrag-euro_2*200-euro_1*100-cent_50*50-cent_20*20-cent_10*10)//5
cent_2=(bedrag-euro_2*200-euro_1*100-cent_50*50-cent_20*20-cent_10*10-cent_5*5)//2
cent_1=(bedrag-euro_2*200-euro_1*100-cent_50*50-cent_20*20-cent_10*10-cent_5*5-cent_2*2)
print("2-euros: ", euro_2)
print("1-euros: ", euro_1)
print("50c-euros: ", cent_50)
print("20c-euros: ", cent_20)
print("10c-euros: ", cent_10)
print("5c-euros: ", cent_5)
print("2c-euros: ", cent_2)
print("1c-euros: ", cent_1)