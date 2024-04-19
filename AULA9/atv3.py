num = int(input("Digite o número:"))
maior = num

for num in range(4):
    num = int(input("Digite o número:"))
    if num > maior:
        maior = num 
print("o maior numero é:",maior)
