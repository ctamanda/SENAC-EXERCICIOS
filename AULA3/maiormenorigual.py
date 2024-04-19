n1 = int(input("digite o primeiro numero:"))
n2 = int(input("digite o segundo numero:"))

if n1>n2: # sempre tem dois pontos 
    print ("O número",n1, "é maior que", n2)
elif n1<n2:  
    print ("O número",n2, "é maior que", n1)
else:  # não tem condição
    print (n1, "é igual", n2)