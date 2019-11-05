Input = input("Type your sentence here: ")
Length = len(Input)
Output = ""
for i in range(Length):
    Backwards = Input[Length - 1 - i]
    Output += Backwards
print(Output, Input, sep=" ")
if Output == Input:
    print(Input, "is a palindrome")
else:
    print(Input, "is not a palindrome")
print("")
