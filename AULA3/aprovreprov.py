#02/04

nota_1 = float(input("digite a primeira nota:"))  #float para números decimais 
nota_2 = float(input("digite a segunda nota:"))   #float para números decimais 

media = (nota_1+nota_2)/2

if  media >= 7:   # se 
    print ("parabéns você aprovado!! sua média foi:",media)
else:             # senão
    print ("aluno reprovado, sua média foi:",media)
