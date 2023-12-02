from math import sqrt

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
        return sqrt(dx * dx + dy * dy)

    def update_center(self):
        sum_x = sum_y = 0

        for point in self.points:
            sum_x += point.x
            sum_y += point.y

        num_points = len(self.points)
        if num_points > 0:
            new_center_x = sum_x / num_points
            new_center_y = sum_y / num_points
            # Faça o novo Centróide C1 ter os valores das médias calculadas em 5.1 e 5.2
            self.center = Point(new_center_x, new_center_y)

    def __str__(self):
        return f'Cluster {self.id} Center: {self.center}\nPoints: {", ".join(map(str, self.points))}\n'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
