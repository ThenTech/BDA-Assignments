number = input("Please enter a number")
even_aantal = 0

for i in number:
    if int(i)%2 == 0:
        even_aantal += 1
print(even_aantal)