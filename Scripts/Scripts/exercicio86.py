matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
coluna3 = []
num = 0
for l in range(3):
  for c in range(3):
    matriz[l][c] = int(input(f"Digite um valor para {[l], [c]}"))


for l in range(3):
  for c in range(3):
    print(f"[{matriz[l][c]:^5}]", end = "")
  print()

for i in matriz:
  for j in i:
    if j % 2 == 0:
      pares.append(j)

for p in matriz:
  coluna3.append(p[2])

for n in matriz[1]:
  if n > num:
    num = n


soma = sum(pares)
col = sum(coluna3)

print(f"a soma dos valores pares é {soma}, a soma dos valores da terceira coluna é {col} e o maior valor da segunda linha é {num} ")
  
  


    
    
