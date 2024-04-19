manga = int(input("Você comprou quantos mangas:"))
total= 0
for i in range (manga):
    valor = float(input("Qual o valor do manga:"))
    total = total+valor
print("O valor total gasto foi de:", total)
print("A media foi de:", total/manga)