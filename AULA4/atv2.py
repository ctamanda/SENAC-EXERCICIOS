#PEÇA AO USUARIO PARA DIGITAR UMA LETRA. 
#IMFORME PARA ELE SE ESSA LETRA É UMA VOGAL OU CONSOANTE.

letra = input("Digite uma letra: ")         # and: se / or: ou 

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":  # sempre começar com a variavel (comparação)
    print("Essa letra é uma vogal.")
else:
    print("Essa letra é uma consoante.")