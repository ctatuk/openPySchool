from datetime import date

def days_to_birtday(month, day):
    today = date.today()
    current_year = date.today().strftime("%Y")
    birthday_in_this_year = date(int(current_year), month, day)
    birthday_in_next_year = date(int(current_year) + 1, month, day)

    if birthday_in_this_year > today:
        result = abs((birthday_in_this_year - today).days)
    else:
        result = abs((birthday_in_next_year - today).days)

    return result

month = 2
day = 10

print(days_to_birtday(month, day))