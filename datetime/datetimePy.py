import datetime

date = datetime.datetime.now()
# print("Current date and time:", date)
# print("Current date:", date.date())
# print("Current time:", date.time())
# print("Current year:", date.year)
# print("Current month:", date.month)
# print("Current day:", date.day)
# print("Current hour:", date.hour)
# print("Current minute:", date.minute)
# print("Current second:", date.second)
# print("Current microsecond:", date.microsecond)
# print("Current weekday:", date.weekday())  # 0=Monday, 1=Tuesday, ..., 6=Sunday
# print("Current ISO calendar:", date.isocalendar())
# seconds since epoch (1970-01-01 00:00:00 UTC)
# print("Current timestamp:", date.timestamp())
# print("Current ISO format:", date.isoformat())
# print("Current RFC 2822 format:", date.strftime("%a, %d %b %Y %H:%M:%S +0000"))

print("Current day", date.strftime("%a"))
print("Current day", date.strftime("%A"))
print("Current day", date.strftime("%w"))
