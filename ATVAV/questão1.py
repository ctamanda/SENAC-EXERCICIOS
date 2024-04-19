# ALISTAMENTO NO EXÉRCITO

sexo = input("Qual o seu sexo? \nobs: digite M para masculino e F para feminino \nDigite: ")
altura = float(input("Qual a sua altura? "))

if sexo == "m" and altura >= 1.70:
    print("Você está apto a se alistar. ")
elif sexo == "f" and altura >= 1.60:
    print("Você está apta a se alistar. ")
else:
    print("Você não está apto(a) a se alistar. ")