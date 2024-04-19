nota = float(input("informe uma nota:"))

while nota<0 or nota>10:
    print("informe uma nuta maior que 0")
    nota = float(input("Informe uma nota 0 a 10:"))
print("Nota inserida com sucesso!")