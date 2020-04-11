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
