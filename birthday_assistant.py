from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    days_of_week = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
        3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            if birthday_this_year.weekday() >= 5:
                birthdays_per_week[days_of_week[0]].append(name)
            else:
                birthdays_per_week[days_of_week[birthday_this_year.weekday()]
                                   ].append(name)

    for day, users_list in birthdays_per_week.items():
        print(f"{day}: {', '.join(users_list)}")


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
    {"name": "Sophia Martinez", "birthday": datetime(1986, 10, 15)},
    {"name": "Joseph Taylor", "birthday": datetime(1992, 10, 17)},
    {"name": "Elizabeth Harris", "birthday": datetime(1977, 10, 18)},
    {"name": "Andrew Wilson", "birthday": datetime(1994, 10, 13)},
    {"name": "Mykyta Moscalew", "birthday": datetime(2010, 2, 8)},
]

get_birthdays_per_week(users)
