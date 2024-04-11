#暴力破解
import itertools
import math
import time

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calculate_distance(city1, city2):
    return math.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)

def total_distance(path, cities):
    total = 0
    for i in range(len(path) - 1):
        total += calculate_distance(cities[path[i]], cities[path[i + 1]])
    total += calculate_distance(cities[path[-1]], cities[path[0]])  # Return to the starting point
    return total

def naive_tsp(cities):
    start_time = time.time()
    num_cities = len(cities)
    min_distance = float('inf')
    min_path = []

    perm = list(range(num_cities))

    for p in itertools.permutations(perm):
        distance = total_distance(p, cities)
        if distance < min_distance:
            min_distance = distance
            min_path = p

    end_time = time.time()
    execution_time = end_time - start_time

    print("Best Path:", end='')
    for city in min_path:
        print(" ", city, end='')
    print()
    print("Minimum Distance:", min_distance)
    print("Execution Time:", execution_time, "seconds")

if __name__ == "__main__":
    nodes = [
        City(60, 200), City(180, 200), City(80, 180), City(140, 180), City(20, 160),
        City(100, 160), City(200, 160), City(140, 140), City(40, 120), City(100, 120)
    ]

    naive_tsp(nodes)
