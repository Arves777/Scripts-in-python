import random
princ = []
temp = []
qnt = int(input("Quantos jogos serão criados? "))


for i in range(qnt + 1):
  for j in range(0, 6):
    x = random.randint(0, 60)
    if x in temp:
      x = random.randint(0, 60)
    temp.append(x)

  princ.append(temp[:])
  temp.clear()
  
  print(f"jogo{i}: {princ[i]} ")
  
