princ = []
nome = []
notas = []
resp = 0


while True:
  nome.append(str(input("Nome: ")))
  notas.append(int(input("Nota 1: ")))
  notas.append(int(input("Nota 2: ")))
  nome.append(notas[:])
  princ.append(nome[:])
  notas.clear()
  nome.clear

  resp = str(input("Quer continuar? (S/N) "))
  if resp in "Nn":
    break

print("-=" * 30)
for i in range(len(princ) + 1):
  média = sum(princ[i][1]) / 2
  print("N°   Nome:   média:")
  print("-" * 30)
  print(f"{i}   princ[i][0]   média")
  

