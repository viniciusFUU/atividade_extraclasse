name = input("Entre com teu nome: ")
age = int(input("Entre com tua idade: "))

if (age <= 10):
    print(f"\n {name} pagará 30 reais.")
elif (age > 10 and age <= 29):
    print(f"\n {name} pagará 60 reais.")
elif (age > 29 and age <= 45):
    print(f"\n {name} pagará 120 reais")
elif (age > 45 and age <= 59):
    print(f"\n {name} pagará 150 reais")
else:
    print(f"\n {name} pagará 400 reais")
