# **Operadores Matemáticos**
# Operações Matemáticas Básicas em Python

n1 = 7
n2 = 2

# 1. Soma
s = n1 + n2        # Soma: 7 + 2 = 9
print(s)           # Saída: 9

s = s + n2         # Soma novamente: 9 + 2 = 11
print(s)           # Saída: 11

s += n2            # Soma com operador abreviado: 11 + 2 = 13
print(s)           # Saída: 13

# 2. Subtração
sub = n1 - n2      # Subtração: 7 - 2 = 5
print(sub)         # Saída: 5

# 3. Multiplicação
mult = n1 * n2     # Multiplicação: 7 * 2 = 14
print(mult)        # Saída: 14

# 4. Divisão Real
div = n1 / n2      # Divisão com resultado decimal: 7 / 2 = 3.5
print(div)         # Saída: 3.5

# 5. Potenciação
pot = n1 ** n2     # Potência: 7 elevado a 2 = 49
print(pot)         # Saída: 49

pot2 = pow(n1, n2) # Outra forma de potência usando a função pow
print(pot2)        # Saída: 49

# 6. Divisão Inteira
divi = n1 // n2    # Retorna apenas a parte inteira: 7 // 2 = 3
print(divi)        # Saída: 3

# 7. Resto da Divisão (Módulo)
rest = n1 % n2     # Resto da divisão: 7 % 2 = 1
print(rest)        # Saída: 1
