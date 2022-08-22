resposta = ""
valores = []
while resposta in "Ss":
  valores.append(int(input("digite um valor: ")))
  resposta = str(input("Quer continuar(S/N)? "))

print(f"a lista possui {len(valores)} números")
valores.sort(reverse = True)
print(f"lista em ordem descrescente: {valores}")
if 5 in valores:
  print("a lista possui o valor 5")
else:
  print("a lista não possui o valor 5")
  
