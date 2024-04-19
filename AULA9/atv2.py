nome = input("Informe o seu nome: ")
while len(nome) <= 2:
    print("Nome invalido.")
    nome = input("Informe o seu nome: ")

idade = int(input("Informe sua idade: "))
while idade <= 150:
    print("Idade invalida.")
    idade = int(input("Informe sua idade: "))

salario = float(input("Informe seu salario: "))
while salario <= 0:
    print("Salario invalido.")
    salario = float(input("Informe seu salario: "))

sexo = input("Qual o seu sexo? \nobs: digite M para masculino e F para feminino \nDigite: ")
while sexo != "m" and sexo != "f":    
    print("Sexo invalido.")
    sexo = input("Qual o seu sexo? \nobs: digite M para masculino e F para feminino \nDigite: ")

estciv = input("Qual o seu estado civil? \nobs: digite 'S' para solteiro, 'C' para casado, 'V' para viuvo e 'D' para divorciado \nDigite: ")
while estciv != "s" and estciv != "c" and estciv != "v" and estciv != "d":
    print("Estado civil invalido.")
    estciv = input("Qual o seu estado civil? \nobs: digite 'S' para solteiro, 'C' para casado, 'V' para viuvo e 'D' para divorciado \nDigite: ")

print("Os dados foram inseridos com sucesso!")

