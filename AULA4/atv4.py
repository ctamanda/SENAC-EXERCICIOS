# FAÇA UM PROGRAMA QUE PERGUNTE EM QUE TURNO VOCE ESTUDA.
# M PARA MATUTINO (bom dia)
# V PARA VESPERTINO (boa tarde)
# N PARA NOTURNO (boa noite)

turno = input("Qual turno você estuda? \nobs: digite M para matutino, V para vespertino e N para noturno \nDigite:")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")   #pode usar quantas x quiser 
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido.")
