nome = input("Nome Completo : ")
print("Analisando o seu nome...")
print(f"seu nome minúsculo é {nome.lower()}")
print(f"seu nome maiúsculo é {nome.upper()}")
print(f"seu nome tem {len(nome)} letras")
nome2 = nome.split()
print(f"seu primeiro nome é {nome2[0]} e possui {len(nome2[0])} letras")
