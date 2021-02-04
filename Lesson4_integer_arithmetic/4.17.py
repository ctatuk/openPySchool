'''
4.17. Известны год и номер месяца рождения человека, а так-
же год и номер месяца сегодняшнего дня (январь – 1 и т. д.). Опре-
делить возраст человека (число полных лет). В случае совпадения
указанных номеров месяцев считать, что прошел полный год.
'''
birth_month = 8
birth_year = 1979
month = 1
year = 2021


def calculate_age(birth_year, birth_month, month, year):
    years = year - birth_year
    if birth_month > month:
        years += 1
    print(years)


calculate_age(birth_year, birth_month, month, year)
