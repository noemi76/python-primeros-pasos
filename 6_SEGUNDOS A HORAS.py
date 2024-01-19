print("CONVERTIDOR DE SEGUNDOS A MINUTOS")
segundos = int(input("Escriba una cantidad de segundos: "))

horas = segundos//3600
resto_1 = segundos%3600
minutos = segundos // 60
resto = segundos % 60
print("{segundos} segundos son {horas} horas, {minutos} minutos y {resto} segundos")