lista = []

for valor in range(5):
    lista.append(valor+10)
print(lista)    

## lsit comprehensions 

lista2 = [valor+10 for valor in range(5)]
print(lista2)

## --------------- outra forma --------------

lista = []
for numero in range (1,30):
  if numero % 4 == 0:
    lista.append(numero)
print(lista)


## com lista compereehension 

multiplo4 = [numero for numero in range(1,30) if numero % 4 == 0] 
print(multiplo4)

## ----------------------------- usando com if e else  

conceito = ['azul' if nota >= 6 else 'vermelho' for nota in range(1,11)]
print(conceito)

conceito = [] 

for nota in range(1,11):
   if nota >= 6:
      conceito.append('azul')
   else:
      conceito.append('vermelho')

    

