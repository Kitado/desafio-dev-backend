import datetime
import calendar


data = input("Informe a data:\n")
data = data.split("/")
dia = datetime.datetime(int(data[2]), int(data[1]), int(data[0]))

somaDias = datetime.timedelta(days = 1)


somaSalario = 0

for i in range(30):
    if calendar.day_name[dia.weekday()] != "Saturday" and calendar.day_name[dia.weekday()] != "Sunday":
        somaSalario += 100
        print(f'{dia} {calendar.day_name[dia.weekday()]} R${somaSalario}')
    dia += somaDias
