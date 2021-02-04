''' Вычислить количство дней до дня рождения в этом году
import time # импортируем модуль time (для работы со всременем)
from datetime import date # импортируем из модуля datetime сегодняшнюю дату
today = date.today() # присваиваем сегоднешней дате имя
today
datetime.date(2021, 1, 25)
today == date.fromtimestamp(time.time()) # возвращение формата data к местному формату времени (летнее время, часовой пояс)?
True
my_birthday = date (today.year, 7, 20) # присваиваю имя к дате "день рождения" в текущем году
if my_birthday < today: # если дата "день рожденя" меньше чем сегодняшний день
    my_birthday = my_birthday.replace(year=today.year+1) # то сегодняшний год увеличь на 1
my_birthday
datetime.date(2021, 7, 20)
time_to_birthday = abs(my_birthday - today) # дней до "дня рождения" = абсолютная величина (день рождение в текущем году минус сегодняшний день)
time_to_birthday.days
176
'''

