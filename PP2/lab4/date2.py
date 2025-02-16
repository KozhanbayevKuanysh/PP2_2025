from datetime import datetime, timedelta

print(f"Yesterday: {datetime.now() - timedelta(days = 1)}")
print(f"Today: {datetime.now()}")
print(f"Tommorow: {datetime.now() + timedelta(days = 1)}")