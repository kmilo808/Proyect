import datetime
now = datetime.datetime.now()
print(now)
fecha_hora_formato = now.strftime("%d-%m-%y")
print(fecha_hora_formato)
hora = now.strftime("%H:%M:%S")
print(hora)