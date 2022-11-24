from datetime import date, datetime, timedelta
import locale

loc = locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


# Class date
# today = date.today()
#
# print(today.weekday())
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.ctime())

# datetime

# now = datetime.now()
#
# print(now, sep='\n')
#
# now = datetime.now()
#
#
# print(f"Date: {now.strftime('%A, %d %b %Y')}")
# print(f"Time: {now.strftime('%H:%M:%S')}")
#
#
# print(now.strftime("%c"))
# print(now.strftime("%x"))
# print(now.strftime("%X"))

now = datetime.today()
print(now.strftime("%c"))
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime("%c"))