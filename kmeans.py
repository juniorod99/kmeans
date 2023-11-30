# Criando um dicionário de coordenadas X e Y
coordenadas = {'ponto1': (1, 1), 
               'ponto2': (1, 2), 
               'ponto3': (2, 2),
               'ponto4': (5, 5),
               'ponto5': (6, 6),
               'ponto6': (7, 7)}

# Acessando coordenadas
for ponto, coordenada in coordenadas.items():
    x, y = coordenada
    print(f'{ponto}: X: {x}, Y: {y}')
