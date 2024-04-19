#FAÇA UM PROGRAMA QUE SOLICITE AO USUARIO O SEU SEXO, (VALORES ACEITOS, M- MASCULINO F- FEMININO)
#RETORNE O MACULINO CASO ELE DIGITE M E F CASO FOR FEMININO, VALOR NÃO PRESENTE CASO DIGITE OUTRA LETR

sexo = input("Qual o seu sexo? \nobs: digite M para masculino e F para feminino \nDigite:")

if sexo == "m":         # == igua / != diferente
    print("seu sexo é: Masculino")
elif sexo == "f":
    print(" Seu sexo é: Feminino")
else:
    print("Sexo não existente.")
