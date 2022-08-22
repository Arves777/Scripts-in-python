matriz = [[],[],[],[],[],[],[],[],[]]
cont = num = 0
cont2 = 0

for i in range(1,10):
  num = int(input(f"Digite um valor para {[cont,cont2]}: "))
  if i == 1:
    matriz[0].insert(0, num)
  elif i == 2:
    matriz[1].insert(0, num)
  elif i == 3:
    matriz[2].insert(0, num)
  elif i == 4:
    matriz[3].insert(0, num)
  elif i == 5:
    matriz[4].insert(0, num)
  elif i == 6:
    matriz[5].insert(0, num)
  elif i == 7:
    matriz[6].insert(0, num)
  elif i == 8:
    matriz[7].insert(0, num)
  elif i == 9:
    matriz[8].insert(0, num)
  elif i == 10:
    matriz[9].insert(0, num)
  
                  
  if i >= 3:
    cont = 1
  if i >= 6:
    cont = 2

  cont2 += 1
  if cont2 > 2:
    cont2 = 0


#print(f"{[matriz[0]}   {[matriz[1]]}   {[matriz[2]]}")
print('{}{}{}'.format(matriz[0],matriz[1],matriz[2]))
print('{}{}{}'.format(matriz[3],matriz[4],matriz[5]))
print('{}{}{}'.format(matriz[6],matriz[7],matriz[8]))
  

    
    
  
