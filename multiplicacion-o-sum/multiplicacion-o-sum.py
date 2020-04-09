"""
Pide al usuario ingresar dos numeros enteros. El programa debera retornar por
pantalla el producto ambos numeros y si este es mayor a 200 entonces retornara la 
suma de ambos numeros. Para esto deberas crear una funcion llamada "multiplicacion_o_sum"
que reciba como input los dos numeros y retorne como output la multiplicacion o suma, segun corresponda.
"""

def multiplicacion_o_sum(n1, n2):
  multiplicacion = n1 * n2
  suma = n1 + n2
  
  if (multiplicacion > 200):
    print("Suma: " + str(suma))
    return
  else:
    print("Multiplicacion: " + str(multiplicacion))
    return

def main():
  n1 = input("Ingresa un numero: ")
  n2 = input("Ingresa otro numero: ")
  
  multiplicacion_o_sum(n1, n2)
  return

main()
   
