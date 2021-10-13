# https://www.hackerrank.com/challenges/calendar-module/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

stdin = list(map(int, input().split()))

day_of_week = calendar.weekday(month=stdin[0], day=stdin[1], year=stdin[2])
stdout = calendar.day_name[day_of_week].upper()

print(stdout)
