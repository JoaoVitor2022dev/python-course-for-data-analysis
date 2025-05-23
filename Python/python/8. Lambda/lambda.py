## lambda

# função normal 
def area_quadrado(l):
    area = l**2
    print(area)

area_quadrado(4) 

#funcção lambda
area_quadrado2 = lambda x: x**2

area_quadrado2(7)

# area de um retangulo 

area_retangulo = lambda b, h: b*h

area_retangulo(4,7)

# lambda com maps 

listas = [4,5,6,7,8,9,10]

area = list(map(lambda x: x**2, listas))
print(area)
