maior = 0
menor = 9000000000000000000
while True:
    num = int(input("Digite um número : "))
    if num > maior:
        maior = num
    if num <= menor:
        menor = num
    confirm=input("Continuar : ")
    if confirm.lower().strip() == "s":
        continue
    elif confirm.lower().strip() == "n":
        break

print(f"O maior valor é : {maior}")
print(f"O menor valor é : {menor}")


