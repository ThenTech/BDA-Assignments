# write your code here

day_born        = int(input)
month_born      = int(input)
year_born       = int(input)

day_current     = int(input)
month_current   = int(input)
year_curent     = int(input)

if month_current < month_born or  (month_current == month_born and day_current <= day_born)
    age = year_current- year_born - 1

if month_current > month_born or (month_current == month_born and day_current > day_born)
    age = year_current - year_born 