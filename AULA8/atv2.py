usuario = input("Informe o nome do usuario:")
senha = input("Informe a senha:")

while senha == usuario:
    print("A senha deve ser diferente do nome!")
    senha = input("Informe a senha:")
print("Senha cadastrada!")