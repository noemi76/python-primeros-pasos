print("CONVERTIDOR DE PIES Y PULGADAS A CENTÍMETROS")
pies = float(input("Escriba una cantidad de pies: "))
pulgadas = float(input("Escriba una cantidad de pulgadas: "))

centimetros = round((pies * 12 + pulgadas) * 2.54,2)

print(pies, "pies y",pulgadas, "pulgadas son", centimetros, "cm")