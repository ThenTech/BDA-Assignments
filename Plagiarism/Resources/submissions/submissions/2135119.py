Input = input("Type your sentence here: ")
Length = len(Input)

for i in range(Length):
    Backwards = Input[Length - 1 - i]
    print(Backwards, end="")
