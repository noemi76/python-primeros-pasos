
print("CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)")
peso = float(input("¿Cuánto pesa? "))
altura = float(input("¿Cuánto mide en metros? "))
   
imc = round((peso / altura ** 2),2)

print("Su imc es: ", imc)
print(
    "Un ímc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,"
)
print(
    "pero esos límites dependen de la edad, del sexo, de la constitución física, etc."
)
