"""
Escriba un programa que haga las veces de cajero. Por ejemplo:
Se le ingresa como input cuanto debe pagar, y cuianto pago. Luego debe mostrar el vuelto.

Ahora para el ejercicio anterior, debe imprimir en pantalla la cantidad de monedas y billetes
que debe entregar, para minimizar la cantidad de billetes y monedas devueltas. 

Todos los valores a pagar terminan en 0 y la minima moneda es de 10 pesos.
Billetes: 20.000, 10.000, 5.000, 2.000, 1.000, 500, 100, 50, 10.
"""

def cajero(pagar, pagado):
  vuelto = pagado - pagar
  return vuelto

def main():
  pagar = int(input("Ingesa cuanto debes pagar: "))
  pagado = int(input("Ingresa cuanto pagaste: "))

  print(cajero(pagar, pagado))

main()