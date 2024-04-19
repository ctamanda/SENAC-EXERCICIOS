#VERIFICADOR DE TRIANGULO

lado1 = float(input("Qual é a medida do lado 1? "))
lado2 = float(input("Qual é a medida do lado 2? "))
lado3 = float(input("Qual é a medida do lado 3? "))

if lado1 == lado2 and lado1 == lado3:
    print ("esse triângulo é equilátero. ")
elif lado1 != lado2 and lado1 != lado3:
    print ("esse triângulo é escaleno. ")
else:
    print("esse triângulo é isósceles.")