saldoM = float(input("Digite seu saldo médio do último ano: "))

if (saldoM <= 500):
    credito = 0
elif (saldoM > 500 and saldoM <= 1000):
    credito = saldoM * 0.3
elif (saldoM > 1000 and saldoM <= 3000):
    credito = saldoM * 0.4
else:
    credito = saldoM * 0.5

if (credito == 0):
    print(f"\n Como seu saldo era de {saldoM}, seu crédito será de {credito}.")
else:
    print(f"\n Como seu saldo era de {saldoM}, seu crédito será de {credito}.")
