import time

today = time.localtime()
input_date = input('Введите дату в формате dd/mm/yyyy  ')
date = time.strptime(input_date, '%d/%m/%Y')

days = int((time.mktime(today) - time.mktime(date))/86400)
print(days)