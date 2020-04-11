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
  ans = []
  bills = [20000, 10000, 5000, 2000, 1000, 500, 100, 50, 10]

  for i in bills:
    if (vuelto // i) > 0:
      ans.extend([i for x in range(vuelto // i)])
      vuelto -= i * (vuelto // i)

  return ans

def main():
  pagar = int(input("Ingesa cuanto debes pagar: "))
  pagado = int(input("Ingresa cuanto pagaste: "))

  vuelto = cajero(pagar, pagado)

  print(
    "Debe entregar " + str(vuelto.count(20000)) + " Billetes de $20.000 \n" +
    "Debe entregar " + str(vuelto.count(10000)) + " Billetes de $10.000 \n" +
    "Debe entregar " + str(vuelto.count(5000)) + " Billetes de $5.000 \n" +
    "Debe entregar " + str(vuelto.count(2000)) + " Billetes de $2.000 \n" +
    "Debe entregar " + str(vuelto.count(1000)) + " Billetes de $1.000 \n" +
    "Debe entregar " + str(vuelto.count(500)) + " Monedas de $500 \n" +
    "Debe entregar " + str(vuelto.count(100)) + " Monedas de $100 \n" +
    "Debe entregar " + str(vuelto.count(50)) + " Monedas de $50 \n" +
    "Debe entregar " + str(vuelto.count(10)) + " Monedas de $10 \n" 
  )



main()