gols2 = []
jogos = {}
partidas = 0

jogos["nome"] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {jogos['nome']} Jogou? "))

print("-=" * 30)
for i in range(partidas):
  gols2.append(int(input(f"Quantos gols na partida {i}? ")))

jogos["total"] = sum(gols2)  
jogos["gols"] = gols2[:]
print("-=" * 30)
for k, v in jogos.items():
  print(f"o campo {k} tem valor {v}")
print("-=" * 30)
print(f"o jogador {jogos['nome']} jogou {partidas} partidas")

for i in range(partidas):
  print(f"na partida {i} fez {jogos['gols'][i]}")

print(f"foi um total de {jogos['total']} gols ")




