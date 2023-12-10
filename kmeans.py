import random
from typing import List

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

class Cluster:
    def __init__(self, _id, center):
        self.id = _id
        self.center = center
        self.points = []

    def limpaPontos(self):
        self.points.clear()

    def addPonto(self, point):
        self.points.append(point)

    def listaPontos(self):
        return [str(ponto) for ponto in self.points]
    
    def exibirCentroid(self):
        centroid = "Centroid {}: {}".format(self.id, self.center)
        print(centroid)
    
    # Calcula distancia do Ponto para o Centroid
    def distanciaParaCentroid(self, point):
        dx = self.center.x - point.x
        dy = self.center.y - point.y
        return (dx ** 2 + dy ** 2) ** 0.5

    # Atualiza posiçao do Centroid com as medias de X e Y 
    def atualizaCentro(self):
        sum_x = sum_y = 0

        for point in self.points:
            sum_x += point.x
            sum_y += point.y

        num_points = len(self.points)
        if num_points > 0:
            new_center_x = sum_x / num_points
            new_center_y = sum_y / num_points
            self.center = Point(new_center_x, new_center_y)

    def __str__(self):
        return f'Centroid {self.id} \nCentro: {self.center}\nPontos: {", ".join(map(str, self.points))}\n'
    

class KMeans:
    def __init__(self, qtdCentroids):
        self.k = qtdCentroids
        self.points = []
        self.clusters = []

    def run(self):
        self.selecionarCentroidAleatorio()
        estaAtualizado = False
        rodada = 1
        while estaAtualizado == False:
            print("------- Rodada {} --------".format(rodada))
            self.showCentroid()
            # Lista contendo Pontos do Centroid antes da atualização
            pA = k_means.getPointsFromClusters()
            # Limpa os pontos que pertence ao Centroid
            self.limpaCentroids()
            # Vincula Pontos ao Cluster mais proximo
            self.vinculaPontosAoCentroid()
            # Lista contendo Pontos do Centroid depois da atualização
            pN = k_means.getPointsFromClusters()
            print(pA)
            print(pN)

            if (pA[0] == pN[0]) or (pA[0] == pN[1]):
                if (pA[1] == pN[0]) or (pA[1] == pN[1]):
                    estaAtualizado = True
                else:
                    estaAtualizado = False

            print('-------------------------')
            print('                              ')
            # Recalcula posiçao do Cluster
            self.attCentroid() 
            rodada += 1

        self.mostraCentroids()

    def vinculaPontosAoCentroid(self):
        for point in self.points:
            # Seleciona Centroid mais proximo ao ponto
            centroidMaisProximo = min(self.clusters, key=lambda cluster: cluster.distanciaParaCentroid(point))
            # Atribui Ponto ao Centroid
            centroidMaisProximo.addPonto(point)

    def attCentroid(self):
        for cluster in self.clusters:
            cluster.atualizaCentro()

    def limpaCentroids(self):
        for cluster in self.clusters:
            cluster.limpaPontos()      

    def showCentroid(self):
        for cluster in self.clusters:
            cluster.exibirCentroid()

    def mostraCentroids(self):
        for cluster in self.clusters:
            print(cluster)

    def getPoints(self):
        for cluster in self.clusters:
            cluster.listaPontos()

    def addPonto(self, x, y):
        self.points.append(Point(x, y))

    def selecionarCentroidAleatorio(self):
        # Seleciona aleatoriamente pontos para clusters terem como coordenada inicial
        centroidAleatorio = random.sample(self.points, self.k)
        self.clusters = [Cluster(i, center) for i, center in enumerate(centroidAleatorio)]
    
    def getPointsFromClusters(self):
        all_points = []
        for cluster in self.clusters:
            points_of_cluster = cluster.listaPontos()
            all_points.append(points_of_cluster)
        return all_points

k_means = KMeans(qtdCentroids = 2)

# Adicionando pontos
k_means.addPonto(1, 1)
k_means.addPonto(9.4, 6.4)
k_means.addPonto(2.5, 2.1)
k_means.addPonto(8, 7.7)
k_means.addPonto(0.5, 2.2)
k_means.addPonto(7.9, 8.4)
k_means.addPonto(7, 7)
k_means.addPonto(2.8, 0.8)
k_means.addPonto(1.2, 3)
k_means.addPonto(7.8, 6.1)

# Executando o algoritmo K-means
k_means.run()

