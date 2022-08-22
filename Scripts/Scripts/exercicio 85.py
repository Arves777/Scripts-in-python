princ = []
pares = []
impares = []
num = 0
cont = 1
for i in range(0,7):
  num = int(input(f"digite o {cont}° número: "))
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)

  
  
  cont += 1
princ.append(pares)
princ.append(impares)
princ[0].sort()
princ[1].sort()
print(f"os numeros pares são {princ[0]} e os numeros impares são {princ[1]}")

