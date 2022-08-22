from datetime import datetime
dados = {}
x = y = 0

dados["nome"] = str(input("Digite seu Nome: "))
x = int(input("Digite seu ano de nascimento: "))
dados["idade"] = datetime.now().year - x
dados["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))
if dados["ctps"] != 0:
  dados["contratação"] = int(input("Ano de contratação: "))
  dados["Salário"] = float(input("Salário: R$ "))
  dados["aposentadoria"] = 35 - (datetime.now().year - dados["contratação"]) + dados["idade"]   

for k, v in dados.items():
  print(f"o {k} tem valor {v}")
