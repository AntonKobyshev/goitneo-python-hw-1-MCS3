from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = datetime.today().date()

    # Створюємо список днів тижня в порядку
    days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Створюємо словник для зберігання імен користувачів за днями тижня
    birthdays_per_week = defaultdict(list)

    # Визначаємо індекс сьогоднішнього дня тижня
    today_index = today.weekday()

    # Проходимо по користувачам і аналізуємо їх дні народження
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Визначаємо різницю в днях між поточною датою і днем народження
        delta_days = (birthday - today).days

        # Визначаємо день тижня дня народження
        day_of_week_index = (today_index + delta_days) % 7

        # Додаємо ім'я користувача до відповідного дня тижня
        birthdays_per_week[days_of_week[day_of_week_index]].append(name)

    # Виводимо результат у порядку днів тижня
    for i in range(7):
        day = days_of_week[(today_index + i) % 7]
        if day in birthdays_per_week:
            print(f"{day}: {', '.join(birthdays_per_week[day])}")


# Приклад використання:
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
