tn = input("Qual é o seu turno e trabalho? \nobs: digite M para matutino, V para vespertino e N para noturno \nDigite: ")
match tn:
    case "m" :
        print("Bom dia!")
    case "v" :
        print("Boa tarde!")
    case "n" :
        print("Boa noite!")
    case _ :
        print("opção inválida.")