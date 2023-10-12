from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    today = datetime.today().date()

    days_of_week = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
        3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }

    birthdays_per_week = defaultdict(list)

    today_weekday = today.weekday()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        delta_days = (birthday - today).days
        day_of_week_index = (today_weekday + delta_days) % 7
        day_of_week = days_of_week[day_of_week_index]

        birthdays_per_week[day_of_week].append(name)

    for i in range(7):
        day = days_of_week[(today_weekday + i) % 7]
        if day in birthdays_per_week:
            print(f"{day}: {', '.join(birthdays_per_week[day])}")


users = [
    {"name": "John Smith", "birthday": datetime(1990, 5, 15)},
    {"name": "Emily Davis", "birthday": datetime(1985, 8, 3)},
    {"name": "David Johnson", "birthday": datetime(1978, 11, 12)},
    {"name": "Sarah Wilson", "birthday": datetime(1993, 4, 27)},
    {"name": "Michael Brown", "birthday": datetime(1982, 7, 8)},
    {"name": "Jessica Lee", "birthday": datetime(1995, 1, 18)},
    {"name": "Daniel Kim", "birthday": datetime(1987, 9, 5)},
    {"name": "Amanda Jones", "birthday": datetime(1989, 6, 30)},
    {"name": "Matthew White", "birthday": datetime(1984, 12, 9)},
    {"name": "Olivia Anderson", "birthday": datetime(1991, 3, 22)},
    {"name": "Christopher Miller", "birthday": datetime(1975, 10, 14)},
    {"name": "Sophia Martinez", "birthday": datetime(1986, 2, 9)},
    {"name": "Joseph Taylor", "birthday": datetime(1992, 7, 7)},
    {"name": "Elizabeth Harris", "birthday": datetime(1977, 6, 25)},
    {"name": "Andrew Wilson", "birthday": datetime(1994, 8, 11)},
    {"name": "Mykyta Moscalew", "birthday": datetime(2010, 2, 8)},
]

get_birthdays_per_week(users)
