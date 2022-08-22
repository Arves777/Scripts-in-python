num = []
cont = 0
for i in range(0, 5):
    valor = int(input("Digite um valor: "))
    if i == 0:
        num.append(valor)
        print("primeiro item da lista")
    if i == 1:
        if valor < num[0]:
            num.insert(0, valor)
            print("foi adicionado na posição 0 da lista")
        else:
            num.insert(1, valor)
            print("foi adicionado na posição 1 da lista")
    if i == 2:
        if valor < num[0]:
            num.insert(0,valor)
            print("foi adicionado na posição 0 da lista")
        elif valor < num[1]:
            num.insert(1, valor)
            print("foi adicionado na posição 1 da lista")
        else:
            num.insert(2, valor)
            print("foi adicionado na posição 2 da lista")
    if i == 3:
        if valor < num[0]:
            num.insert(0,valor)
            print("foi adicionado na posição 0 da lista")
        elif valor < num[1]:
            num.insert(1, valor)
            print("foi adicionado na posição 1 da lista")
        elif valor < num[2]:
            num.insert(2, valor)
            print("foi adicionado na posição 2 da lista")
        else:
            num.insert(3, valor)
            print("foi adicionado na posição 3 da lista")

    if i == 4:
        if valor < num[0]:
            num.insert(0,valor)
            print("foi adicionado na posição 0 da lista")
        elif valor < num[1]:
            num.insert(1, valor)
            print("foi adicionado na posição 1 da lista")
        elif valor < num[2]:
            num.insert(2, valor)
            print("foi adicionado na posição 2 da lista")
        elif valor < num[3]:
            num.insert(3, valor)
            print("foi adicionado na posição 3 da lista")
        else:
            num.insert(4, valor)
            print("foi adicionado na posição 4 da lista")

    if i == 5:
        if valor < num[0]:
            num.insert(0,valor)
            print("foi adicionado na posição 0 da lista")
        elif valor < num[1]:
            num.insert(1, valor)
            print("foi adicionado na posição 1 da lista")
        elif valor < num[2]:
            num.insert(2, valor)
            print("foi adicionado na posição 2 da lista")
        elif valor < num[3]:
            num.insert(3, valor)
            print("foi adicionado na posição 3 da lista")
        elif valor < num[4]:
            num.insert(4, valor)
            print("foi adicionado na posição 4 da lista")
        else:
            num.insert(5, valor)
            print("foi adicionado na posição 5 da lista")
print(num)
    
        
        
        
        
                
        
        
    
        
    
