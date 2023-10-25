import random
from itertools import permutations
import math
import matplotlib.pyplot as plt

MAX_SIZE = 5000


def generate_point_in_area():
    return round(random.randint(0, MAX_SIZE)), round(random.randint(0, MAX_SIZE))


def two_points_distance(p1, p2):
    return math.dist(p1, p2)


def distance_matrix(points):
    n = len(points)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = two_points_distance(points[i], points[j])
    return matrix


def TSP(s, e, points, k):
    min_path = None
    min_distance = float('inf')

    points = [p for p in points if p != s and p != e]

    for p in permutations(points, k):
        total_dist = two_points_distance(s, p[0]) + two_points_distance(p[-1], e)
        for i in range(len(p) - 1):
            total_dist += two_points_distance(p[i], p[i + 1])
        if total_dist < min_distance:
            min_distance = total_dist
            min_path = (s,) + p + (e,)
    return min_path, min_distance


random.seed(1234)

n = 20

points_cords = [generate_point_in_area() for _ in range(n)]
start = random.choice(points_cords)
end = random.choice(points_cords)

while end == start:
    end = random.choice(points_cords)

k = random.randint(1, n-2)
path, dist = TSP(start, end, points_cords, k)
print("Shortest Path:", path)
print("Distance:", dist)



###############for testing purposes
def plot_graph(start, end, path, points_cords):
    plt.figure(figsize=(10, 10))

    # Plot all points
    xs, ys = zip(*points_cords)
    plt.scatter(xs, ys, color='blue', s=100, zorder=5)
    for point, x, y in zip(points_cords, xs, ys):
        plt.text(x, y, str(point), fontsize=12, ha='right')

    # Plot start and end points
    plt.scatter(*start, color='green', s=150, label='Start', zorder=5)
    plt.scatter(*end, color='red', s=150, label='End', zorder=5)

    # Plot the shortest path
    path_x, path_y = zip(*path)
    plt.plot(path_x, path_y, color='purple', lw=2, zorder=1)

    plt.title("Shortest Path using TSP")
    plt.grid(True)
    plt.legend()
    plt.xlim(0, MAX_SIZE)
    plt.ylim(0, MAX_SIZE)
    plt.show()


plot_graph(start, end, path, points_cords)