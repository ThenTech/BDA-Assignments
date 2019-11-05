day_st = int(input("dayst"))
month_st = int(input("monthst"))
year_st = int(input("yearst"))
day_end = int(input("dayend"))
month_end = int(input("motnhend"))
year_end = int(input("yearend"))
year_counter = -1
while year_end != year_st:
    year_end -= 1
    year_counter += 1
while month_end != 0:
    if month_end == month_st:
        while day_end != 0:
            if day_end == day_st:
                year_counter += 1
            day_end -= 1
    month_end -= 1

print(year_counter)