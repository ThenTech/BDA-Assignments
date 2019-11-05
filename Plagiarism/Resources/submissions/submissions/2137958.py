# write your code here
birth_day = int(input())
birth_month = int(input())
birth_year = int(input())

curr_day = int(input())
curr_month = int(input())
curr_year = int(input())

total_birth_days = birth_day + birth_month * (365 // 12) + birth_year * 365
total_curr_days = curr_day + curr_month * (365 // 12) + curr_year * 365

print((total_curr_days - total_birth_days) // 365)