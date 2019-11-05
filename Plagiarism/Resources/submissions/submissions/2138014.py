dayb = int(input('Day born?'))
monb = int(input('Month born?'))
yearb = int(input('year born?'))
dayt = int(input('Day today?'))
mont = int(input('Month today?'))
yeart = int(input('year today?'))

if dayt - dayb < 0:
    monb += 1
if mont - monb < 0:
    yearb += 1
print(yeart - yearb)
