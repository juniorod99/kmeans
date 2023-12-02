import random
from typing import List
from Cluster2 import Cluster
from Point import Point

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

    def clear_points(self):
        self.points.clear()

    def add_point(self, point):
        self.points.append(point)

    def get_distance_to_center(self, point):
        dx = self.center.x - point.x
        dy = self.center.y - point.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def update_center(self):
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
        return f'Cluster {self.id} Center: {self.center}\nPoints: {", ".join(map(str, self.points))}\n'


class KMeans:
    def __init__(self, k, max_iterations):
        self.k = k
        self.max_iterations = max_iterations
        self.points = []
        self.clusters = []

    def run(self):
        self.initialize_clusters()
        iteration = 0
        is_updated = True

        while iteration < self.max_iterations and is_updated:
            self.clear_clusters()
            is_updated = self.assign_points_to_clusters()
            self.update_cluster_centers()
            iteration += 1

        self.print_clusters()

    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def initialize_clusters(self):
        random_centers = random.sample(self.points, self.k)
        self.clusters = [Cluster(i, center) for i, center in enumerate(random_centers)]
        

    def clear_clusters(self):
        for cluster in self.clusters:
            cluster.clear_points()
            

    def assign_points_to_clusters(self):
        is_updated = False

        for point in self.points:
            # print('teste')
            nearest_cluster = min(self.clusters, key=lambda cluster: cluster.get_distance_to_center(point))
            nearest_cluster.add_point(point)
            is_updated = True

        return is_updated

    def update_cluster_centers(self):
        for cluster in self.clusters:
            cluster.update_center()
            

    def print_clusters(self):
        for cluster in self.clusters:
            print(cluster)


# Exemplo de uso
k_means = KMeans(k=2, max_iterations=100)

# Adicionando pontos
k_means.add_point(1, 1)
k_means.add_point(1, 2)
k_means.add_point(2, 2)
k_means.add_point(5, 5)
k_means.add_point(6, 6)
k_means.add_point(7, 7)
# Adicione mais pontos conforme necessário...

# Executando o algoritmo K-means
k_means.run()
