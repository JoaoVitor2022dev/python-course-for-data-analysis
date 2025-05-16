# -------------------------------------------
# FOR COM RANGE
# -------------------------------------------
# Utiliza o range para controlar o número de repetições (início, fim)

for x in range(0, 4):
    print(x)  # Saída: 0, 1, 2, 3

# -------------------------------------------
# FOR PARA PERCORRER UMA LISTA
# -------------------------------------------

lista = [1, 2, 3, 4, 10]

for numero in lista:
    mult = numero * 2
    print(mult)  # Imprime o dobro de cada número da lista

# -------------------------------------------
# IF + FOR - ESTRUTURA CONDICIONAL COM REPETIÇÃO
# -------------------------------------------
# Lê 5 valores digitados pelo usuário
# Soma apenas os valores pares e conta quantos são

soma = 0
cont = 0

for x in range(1, 6):
    num = int(input('Digite o {}º valor: '.format(x)))
    if num % 2 == 0:
        soma += num
        cont += 1

print('Você informou {} números pares e a soma deles é igual a {}'.format(cont, soma))

# -------------------------------------------
# WHILE - REPETIÇÃO BASEADA EM CONDIÇÃO
# -------------------------------------------
# Executa o bloco enquanto a condição for verdadeira

c = 1  

while c < 10:
    s = c + 10
    print(s)
    c += 1

print('Fim')
