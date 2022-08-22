resposta = ""
dados = []
maispes = []
maislev = []
pessoas = []
pes = lev = pessoa = 0
cont = nome = 0
dados = []
while resposta not in "Nn":
  nome = int(input(""))
  peso = int(input("Digite seu peso: "))
  dados.append(nome)
  dados.append(peso)
  if cont == 0:
    pes = peso
    lev = peso
    pessoa1 = nome

  if cont > 0:
    pessoa2 = nome
    if pes < peso:
      pessoas.append(pessoa)
      maispes.append(peso)
      maispes.append(pessoas)
    elif pes == peso:
      pessoas.append(pessoa1)
      pessoas.append(pessoa2)
      maispes.append(peso)
      maispes.append(pessoas)
    if lev > peso:
      pessoas.append(pessoa)
      maislev.append(peso)
      maislev.append(pessoas)
    elif lev == peso:
      pessoas.append(pessoa1)
      pessoas.append(pessoa2)
      maislev.append(peso)
      maislev.append(pessoas)

  cont += 1

print(f"foram cadastradas {cont} pessoas")
print(f"o maior peso cadastrado foi {maispes[0]} de {maispes[1]}")
print("e o menor peso cadastrado foi {maislev[0]} de {maispes[1]}")
        
