import datetime
a = datetime.date.today()
print(a)
year = int(input())
month = int(input())
day = int(input())
b = datetime.date(year, month, day)
print(b)
c = a-b
print(c)
