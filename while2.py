#Adivinar un numero con pistas hechas por el programa.
numero_entero = int(input("Escriba un numero entero"))
while numero_entero != 25:
 if numero_entero < 25:
    print ("El numero es mayor")
 else:
    print ("El numero es menor")

 numero_entero = int(input("No es el numero correcto vuelva a intentarlo"))

print("Enhorabuena")



