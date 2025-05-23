# ============================
#        LISTAS [ ]
# ============================

print("======= LISTAS =======")

# Criando uma lista
num = [2, 5, 7, 9]
print("Lista original:", num)

# Substituindo o elemento da posição 3 (número 9) por 4
num[3] = 4
print("Após substituir o índice 3 por 4:", num)

# Adicionando o número 8 ao final da lista
num.append(8)
print("Após adicionar o número 8:", num)

# Ordenando a lista em ordem crescente
num.sort()
print("Lista ordenada:", num)

# Inserindo o número 0 na posição 2
num.insert(2, 0)
print("Após inserir 0 na posição 2:", num)

# Removendo o elemento da posição 3
num.pop(3)
print("Após remover o elemento da posição 3:", num)


# ============================
#        TUPLAS ( )
# ============================

print("\n======= TUPLAS =======")

# Tuplas são imutáveis
num2 = (2, 5, 7, 9)
print("Tupla original:", num2)


# ============================
#      DICIONÁRIOS { }
# ============================

print("\n===== DICIONÁRIOS =====")

# Criando um dicionário com informações de uma pessoa
pessoas = {
    'nome': 'Luciano',
    'sexo': 'masculino',
    'idade': 46
}
print("Dicionário original:", pessoas)

# Adicionando uma nova chave com valor
pessoas['time'] = 'Corinthians'
print("Após adicionar 'time':", pessoas)

# Removendo a chave 'idade' do dicionário
del pessoas['idade']
print("Após remover 'idade':", pessoas)
