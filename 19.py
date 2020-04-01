#!/usr/bin/env python

days = (365 * 100) + 24
months = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31} 
leap_months = {0:31, 1:29, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 
        11:31}

sunday_list = []
for day in range(1, days+1):
    if (day % 7 == 0):
        sunday_list.append(day)

first_of_month_list = []
years = 1901
days = 1
while (years < 2001):
    if (days % 365 == 0):
        years += 1
    if (years % 4 == 0):
        for month in leap_months:
            days += leap_months[month]
            first_of_month_list.append(days)
    else:
        for month in months:
            days += months[month]
            first_of_month_list.append(days)
    days += 1

count = 0
for day in sunday_list:
    if day in first_of_month_list:
        count += 1
print(count)
