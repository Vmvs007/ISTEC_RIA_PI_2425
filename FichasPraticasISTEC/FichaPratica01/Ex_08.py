totalSegundosAlbum = 0

# Ler duração das músicas

# Música 1
minutosLidos = int(input("Insira os minutos da 1º música: "))
segundosLidos = int(input("Insira os segundos da 1º música: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

# Música 2
minutosLidos = int(input("Insira os minutos da 2º música: "))
segundosLidos = int(input("Insira os segundos da 2º música: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

# Música 3
minutosLidos = int(input("Insira os minutos da 3º música: "))
segundosLidos = int(input("Insira os segundos da 3º música: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

# Música 4
minutosLidos = int(input("Insira os minutos da 4º música: "))
segundosLidos = int(input("Insira os segundos da 4º música: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

# Música 5
minutosLidos = int(input("Insira os minutos da 5º música: "))
segundosLidos = int(input("Insira os segundos da 5º música: "))

totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

print("Total Segundos:", totalSegundosAlbum)

# Calcular a duração do album hh:mm:ss

horas = totalSegundosAlbum // 3600

totalSegundosAlbum = totalSegundosAlbum % 3600

minutos = totalSegundosAlbum // 60

totalSegundosAlbum = totalSegundosAlbum % 60

segundos = totalSegundosAlbum

print(horas, ":", minutos, ":", segundos)
