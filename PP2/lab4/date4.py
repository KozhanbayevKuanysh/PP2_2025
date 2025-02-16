from datetime import datetime, timedelta

x = datetime(year = 2020, month = 2, day = 20, hour = 12, minute = 50, second = 25)
y = datetime(year = 2020, month = 2, day = 20, hour = 12, minute = 40, second = 12)

print((x - y).total_seconds())