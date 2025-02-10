horas = int(input("Insira as horas: "))
minutos = int(input("Insira os minutos: "))

if (horas > 12):
    horas = horas - 12
    print(horas, ":", minutos, "PM")
else:
    print(horas, ":", minutos, "AM")
