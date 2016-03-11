date = raw_input("Input a date in form dd/mm/yyyy (e.g 05/12/1997)")

date = date.split("/")

day = date [0]
month = date [1]
year = date [2]

day = int(day)
month = int(month)
year = int(year)

daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if month < 3:
    z = year-1
else:
    z = year
x = (23*month//9 + day + 3 + year + z//4 - z//100 + z//400)
if month >= 3:
    x = x-2

x = x % 7

DayOfWeek = daysOfTheWeek[x]
print DayOfWeek

#source:
#http://stackoverflow.com/questions/9847213/which-day-of-week-given-a-date-python
#http://code.activestate.com/recipes/266464-date-to-day-of-the-week/
