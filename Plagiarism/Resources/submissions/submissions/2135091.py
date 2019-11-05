birthDay = int(input())
birthMonth = int(input())
birthYear = int(input())

currDay = int(input())
currMonth = int(input())
currYear = int(input())

age = currYear - birthYear

if birthMonth > currMonth:
    age -= 1
    
elif birthMonth == currMonth:
    if birthDay > currDay: 
        age -= 1
        
print(age)