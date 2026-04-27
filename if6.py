#Calcular el salario de un empleado
hours = int(input("Ingrese sus horas laborales"))
pago_hora= int(input("Ingrese el pago por hora trabajada"))
resultado = pago_hora * hours
print (f"Su salario es: {resultado}")
if resultado > 2000000:
 print("Gana mas del salario minimo")
elif resultado == 2000000:
 print ("Gana el salario minimo")
else:
 print("Gana menos del salario minimo")
