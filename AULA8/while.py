acumulador = 0 
num = int(input("informe um número:"))

while num != 0:
    #acumulador = acumulador + num 
    acumulador += num 
    num = int(input("informe um número:"))
print(acumulador)