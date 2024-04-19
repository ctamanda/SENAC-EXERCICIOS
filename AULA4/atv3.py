
# Qual dos 3 numeros é maior

num1 = int(input("digite um número:"))
num2 = int(input("digite um número:"))
num3 = int(input("digite um número:"))

if num1 > num2 and num1 > num3:
    print("O maior número é: ",num1 )
elif num2 > num1 and num2 > num3:
    print("O maior número é: ",num2 )
else:
    print("O maior número é: ",num3 )