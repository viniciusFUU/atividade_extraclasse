x = float(input("Digite o valor de X: "))

if (x > 4.0 or x < (-4.0)):
    fx = (5*x+3)/(x**2-16)**0.5
    print(f"\nf(x) = {fx}")
else:
    print("\nNão pode ser feita.")