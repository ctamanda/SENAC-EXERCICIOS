conv =  int(input("Escolha um opção \n 1- Converter de Celsius para Fahrenheit \n 2- converter de Fahrenheit para Celsius \n Digite: "))
temp = float(input("Qual é a temperatura? "))

match conv:
    case 1 :
        print("A temperatura em Fahrenheit é", (temp*9/5)+32 )
    case 2 :
        print("A temperatura em Fahrenheit é", (temp-32)*5/9 )
    case _ :
        print("opção inválida.")
