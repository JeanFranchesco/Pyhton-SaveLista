lista1=[]
lista2=[]

for x in range(0,5):
  num = int(input("Digite o que deseja salvar na lista 1: "))
  lista1.append(num)
for y in range(0,5):
  num = int(input("Digite o que deseja salvar na lista 2: "))
  lista2.append(num)

print("Lista 1",lista1)
print("Lista 2",lista2)
setLista1=set(lista1)
setLista2=set(lista2)
lista3=setLista1.union(setLista2)
print("União da Lista 1 e Lista 2:", lista3)

comum=setLista1.intersection(setLista2)
print("Interseção da Lista 1 e Lista 2:", comum)

diferente=setLista1.difference(setLista2)
diferente2=setLista2.difference(setLista1)
print("Itens em Lista 1 e não em Lista 2:", diferente)
print("Itens em Lista 2 e não em Lista 1:", diferente2)

