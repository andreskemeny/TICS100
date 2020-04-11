"""
Pide al usuario que ingrese un numero.
El programa debera retornar por pantalla si el numero es par o impar.
Si el numero es multiplo de 4 debera retornar por pantalla un mensaje diferente
"""

def check(num):
  if (num % 4) == 0:
    return "Numero multiplo de 4"
  else:
    if (num % 2) == 0:
      return "Numero par"
    else:
      return "Numero impar"

def main():
  num = int(input("Ingresa un numero: "))
  print(check(num))

main()
