import random
from operator import itemgetter
dic = {"jogador1": random.randint(1, 6),
       "jogador2": random.randint(1, 6),
       "jogador3": random.randint(1, 6),
       "jogador4": random.randint(1, 6)}
rank = []

print("valores sorteados: ")
for k, v in dic.items():
  print(f"o {k} tirou {v}")

rank = sorted(dic.items(), key= itemgetter(1), reverse = True)
print("-=" * 30)
print("Ranking dos jogadores: ")
print("-=" * 30)
for i, v in enumerate(rank):
  print(f"{i + 1}° lugar: {v[0]} com {v[1]}")
  
  





    
  
  
