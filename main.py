#menu principal
from funciones import suma, resta, multiplicacion, division

while True:
   """
   1)Suma
   2)Resta
   3)Multiplicacion
   4)Division
   5)Salir
   """
   opcion = int(input("Seleccione su opcion: "))
   if opcion == 1:
       num1 = int(input("Ingrese el primer numero: "))
       num2 = int(input("Ingrese el segundo numero: "))
       suma(num1, num2)
