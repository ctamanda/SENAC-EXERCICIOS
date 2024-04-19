# CONVERSOR DE TEMPERATURA

conv =  input("Escolha um opção \n A- Converter de Celsius para Fahrenheit \n B- converter de Fahrenheit para Celsius \n Digite: ")
temp = float(input("Qual é a temperatura? "))

if conv == "a":
    print("A temperatura em Fahrenheit é", (temp*9/5)+32 )
else:
    print("A temperatura em Fahrenheit é", (temp-32)*5/9 )