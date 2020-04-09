"""
Escribe un programa que pueda transformar temperaturas de Fahrenheit a Celsius y viceversa. 
(Formula: c/5 = f-32/9 , donde c: temperatura en Celsius y f: temperatura en Fahrenheit). 
Debe retornar el valor redondeado. 
Output esperado:
60.0 grados c son 140 grados Fahrenheit
45.0 grados f son 7 grados Celsius
"""

def c_to_f(c):
  f = ((9 * c) + 160)/5
  return f

def f_to_c(f):
  c = (5 * (f - 32))/9
  return c

def main():
  running = True
  
  while running:
    try:
      operation = int(input("Ingresa 0 si quieres convertir de C a F, 1 si quieres convertir de F a C, 2 para salir: "))

      if (operation == 0):
        t = int(input("Ingresa la temperatura que deseas transformar: "))
        print(c_to_f(t))
      elif (operation == 1):
        t = int(input("Ingresa la temperatura que deseas transformar: "))
        print(f_to_c(t))
      else:
        break
    except NameError:
      print("Ingresa 1 si quieres convertir de C a F, 0 si quieres convertir de F a C: ")
      continue

  print("Adios!")
    

main()