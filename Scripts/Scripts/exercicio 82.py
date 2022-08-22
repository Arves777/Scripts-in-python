resposta =  ""
valores = []
pares = []
impares = []
while resposta  in "Ss":
  valores.append(input("Digite um valor: "))
  resposta = input("Quer continuar(S/N)? ")

for i in valores:
  modulo = int(i) % 2
  if modulo == 0:
    pares.append(i)
  else:
    impares.append(i)

print(f"a lista valores é formada por: {valores}")
print(f"a lista pares é formada por: {pares}")
print(f"a lista impares é formada por: {impares}")

