
compra = float(input("Qual é o valor da sua compra? "))
pagamento = input("Débito ou crédito? \nobs: digite D para débito e C para crédito. \nDigite: ")

if pagamento == "d":
    print("O valor é: ",compra*0.95)
elif pagamento == "c":
    print("O valor é: ",compra)
else:
    print("valor inválido")