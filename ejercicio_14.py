##import random
from random import randint
elementos=["pera","uva","manzana"]

for ele in elementos:
    print(ele)

milista = []

##nueva lista
for i in range(10):
    milista.append(randint(1,20))
for elemento in milista:
    print(elemento)
