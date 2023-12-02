class Cluster:
    def __init__(self, objeto_id, coordenada_x, coordenada_y):
        self.id = objeto_id
        self.x = coordenada_x
        self.y = coordenada_y
        self.pontos = []

    def adicionar_objeto(self, outro_objeto):
        self.pontos.append(outro_objeto)

    def mostrar_pontos(self):
       for ponto in self.pontos:
        print(f"ID: {ponto}") 