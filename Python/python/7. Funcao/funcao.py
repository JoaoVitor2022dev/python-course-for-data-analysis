# Função com retorno de uma string
def identificacao(nome, idade):
    print(f"Olá, {nome}!\nVocê é jovem e tem apenas {idade} anos de idade.")

# Entrada de dados
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

# Chamada da função
identificacao(nome, idade)


# Função para identificar o maior número entre dois
def maior(x, y):
    if x < y:
        print(f"O maior número é {y}")
    elif x == y:
        print("Os números são iguais.")
    else:
        print(f"O maior número é {x}")

# Chamada da função
maior(21, 21)


# Função com expressões matemáticas (Teorema de Pitágoras)
def pitagoras(cat1, cat2, hip):
    if hip == '?':
        hip = (cat1 ** 2 + cat2 ** 2) ** 0.5
        print("A hipotenusa é:", round(hip, 2))
    elif cat1 == '?':
        cat1 = (hip ** 2 - cat2 ** 2) ** 0.5
        print("O cateto 1 é:", round(cat1, 2))
    elif cat2 == '?':
        cat2 = (hip ** 2 - cat1 ** 2) ** 0.5
        print("O cateto 2 é:", round(cat2, 2))
    else:
        print("Todos os lados estão definidos. Nada a calcular.")

# Chamada da função
pitagoras(3, '?', 5)
