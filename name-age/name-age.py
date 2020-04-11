"""
Pide al usuario que ingrese su nombre y luego su edad. 
El programa debera retornar por pantalla el ao en que el usuario cumplira 100 aos.
Ejemplo: si el usuario de nombre 'Berlini' ingresa que tiene 30 aos debera imprimir
por pantalla: 'Berlini, cumpliras 100 aos el ao 2090'
"""

def main():
  name = raw_input("Ingresa tu nombre: ")
  age = int(input(u"Ingresa la edad que cumples este ao: "))

  yr = 2020 + (100 - age)

  print(name + u", cumpliras 100 a\xf1os el a\xf1o " + str(yr))

main()


