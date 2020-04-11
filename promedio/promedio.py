"""
Escriba un programa que permita calcular el promedio de 3 notas,
estas tres notas deben ser ingresadas por el usuario
"""

def promedio(n1, n2, n3):
  promedio = float((n1 + n2 + n3)/3)
  return promedio

def main():
  n1 = float(input("Ingresa el primer numero: "))
  n2 = float(input("Ingresa el segundo numero: "))
  n3 = float(input("Ingresa el tercer numero: "))

  print(promedio(n1, n2, n3))

main()