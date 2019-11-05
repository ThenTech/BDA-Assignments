days = input('How many days?')
hours = input('How many minutes?')
mindays = int(days)*1440
minhours = int(hours)*60
minutes = int(mindays)+int(minhours)
print(minutes)