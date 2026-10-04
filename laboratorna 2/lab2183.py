from datetime import date, timedelta

day = int(input())
month = int(input())
year = int(input())

yesterday = date(year, month, day) - timedelta(days=1)

print(f"{yesterday.day}.{yesterday.month}.{yesterday.year}")