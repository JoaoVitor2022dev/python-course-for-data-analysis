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

raiz3 = sqrt(64)
print(f'{raiz3:.2}')






