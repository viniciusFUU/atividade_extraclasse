import math as m

pi = 3.14
ang = float(input("Digite o ângulo em graus: "))
rang = ang * pi / 180

if (rang > pi/2 and rang <= pi or rang > 3*pi/2 and rang <= 2*pi):
    print(f"\n Seno: {m.sin(rang):.5f}")
else:
    print(f"\n Co-seno: {m.cos(rang):.5f}")
