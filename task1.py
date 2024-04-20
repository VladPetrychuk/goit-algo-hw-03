from datetime import datetime

def get_days_from_today(date):
    try:
        date_str = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today().date()
        diff = today - date_str.date()

        return diff.days
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
        return None

print(get_days_from_today("2021-10-09")) 