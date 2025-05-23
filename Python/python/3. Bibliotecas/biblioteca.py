import numpy as np
import math

n = 18 

raiz = math.sqrt(n)
# Esta é a função format para colcoar valores com variaveis dentro de strings, w :.2f é para colocar 2 casas 
# decimais
print('A raiz de {} é igual a {:.2f}'.format (n ,raiz))

# Uma alternativa do format
print(f'A raiz de {n} é igual a {raiz:.2f}')

# outra forma de executar uma razi quadrada sem a biblioteca 
raiz2 = n ** 0.5
print(f'{raiz2:.3f}')

# Renomeando o math para sqrt para poder refatorar o código
from math import sqrt

raiz3 = sqrt(16)
print(f'{raiz3:.2}')

# impotantando funcção matematica, valor fatorial 

from math import sqrt, factorial

fat = factorial(4)

print(f'valor fatorial {fat}')     # valor fatorial 5! 5.4.3.2 = 120


# O fatorial não pode fazer o calculo com numero fracionado 

faturial_raiz = factorial(int(sqrt(16)))

faturial_raiz

# Números aleatório com a radon

from random import random, randint 

num = randint(1,10)

print(num)

radonnum = random()

print(radonnum)






