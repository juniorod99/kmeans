import random
from Cluster import Cluster


# Criando um dicionário de coordenadas X e Y
coordenadas = {'p1': (1, 1), 
               'p2': (1, 2), 
               'p3': (2, 2),
               'p4': (5, 5),
               'p5': (6, 6),
               'p6': (7, 7)}

c1 = Cluster(objeto_id=1, coordenada_x=1, coordenada_y=2)
c2 = Cluster(objeto_id=2, coordenada_x=2, coordenada_y=2)
c1.adicionar_objeto(coordenadas['p1'])
c1.mostrar_pontos()

# # Acessando coordenadas
# for ponto, coordenada in coordenadas.items():
#     x, y = coordenada
#     print(f'{ponto}: X: {x}, Y: {y}')

# # Clusters
# clusters = {'c1': ()}
# c1 = coordenadas['p2']
# c2 = coordenadas['p3']


# print(f'Valor Correspondente: {c1}')
# print(f'Valor Correspondente: {c2}')
