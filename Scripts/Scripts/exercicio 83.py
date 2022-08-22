expr =str((input("Digite a expressão: ")))
pi = expr.count("(")
pf = expr.count(")")

if expr.index("(") < expr.index(")"):
  if pi == pf:
    print("sua expressão é válida! ")
  else:
    print("sua expressão é inválida! ")
else:
  print("sua expressão é inválida")


