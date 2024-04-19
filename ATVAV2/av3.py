eleitor= int(input("Qual a quantidade de eleitores? "))
print ("2021- Tião do Gás""\n2403- Shaolin matador de porco""\n1202- Zé da manga")
tiao = 0
shaolin = 0 
ze = 0 
for i in range(eleitor):
    vot = int(input("Digite o número do seu eleitor? "))
    if vot == 2021:
        tiao += 1
    elif vot == 2403:
        shaolin += 1
    elif vot == 1202:
        ze += 1
print("O candidato Tião do Gás rebeceu:", tiao, "votos")
print("O Shaolin matador de porco rebeceu:", shaolin, "votos")
print("O candidato Zé da manga rebeceu:", ze, "votos")
