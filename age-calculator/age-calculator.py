"""
Considere un programa que reciba las variables tipo (int) i, j, k, l, m, n las cuales toman el valor del año(i), mes(j), día(k) 
en el que nació una persona y año(l), mes(m), día(n) en el que estamos respectivamente. 
Usted debe retornar al usuario por pantalla la edad en años que tiene.
"""

def calculateAge(currentYear, currentMonth, currentDay, birthYear, birthMonth, birthDay):
  try:
    if (currentYear < birthYear):
      print("El año actual no puede ser menor que el año en que naciste.")
      return

    years = currentYear - birthYear
    months = currentMonth - birthMonth
    days = currentDay - birthDay

    if (months < 0):
      years -= 1
      months = (12 + months) - 1
      days = currentDay

    print("Tienes", years, "con", months, "meses", "y", days, "días.")
    return 
  except ValueError:
    print("Los inputs deben ser numeros.")
    return

def main():
  currentYear = int(input("Año actual: "))
  currentMonth = int(input("Mes actual: "))
  currentDay = int(input("Día (numero) actual: "))

  birthYear = int(input("Año que naciste: "))
  birthMonth = int(input("Mes que naciste: "))
  birthDay = int(input("Dia (numero) que naciste: "))

  if (-10**9 <= birthYear <= 10**9 and -10**9 <= currentYear <= 10**9):
    if (1 <= birthMonth <= 12 and 1 <= currentMonth <= 12):
      if(1 <= birthDay <= 31 and 1 <= currentDay <= 31):
        calculateAge(currentYear, currentMonth, currentDay, birthYear, birthMonth, birthDay)
        return
      else:
        print("\n Error: Los días deben ser numeros en el intervalo [1, 31] \n")
        main()
    else:
      print("\n Error: Los meses deben ser numeros en el intervalo [1, 12] \n")
      main()
  else:
    print("\n Error:Los años deben ser numeros en el intervalo [-10**9, 10**9] \n")
    main()

main()





