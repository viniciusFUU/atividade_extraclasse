peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso/altura**2

if (imc <= 20):
    print(f"\n Seu IMC é de {imc:.2f}, você está abaixo do peso.")
elif (imc > 20 and imc <= 25):
    print(f"\n Seu IMC é de {imc:.2f}, você está normal.")
elif (imc > 25 and imc <= 30):
    print(f"\n Seu IMC é de {imc:.2f}, você está com excesso de peso.")
elif (imc > 30 and imc <= 35):
    print(f"\n Seu IMC é de {imc:.2f}, você está obeso.")
else:
    print(f"\n Seu IMC é de {imc:.2f}, você está com obesidade morbida")
