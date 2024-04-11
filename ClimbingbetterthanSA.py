#爬山演算法 vs 退火演算法 退火較差
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(city1, city2):
    return np.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)

def total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        total += distance(path[i], path[i + 1])
    total += distance(path[-1], path[0])  # 回到起點
    return total

def hill_climbing_tsp(nodes):
    current_path = nodes.copy()
    current_distance = total_distance(current_path)

    improved = True
    while improved:
        improved = False
        for i in range(len(nodes) - 1):
            for j in range(i + 1, len(nodes)):
                current_path[i], current_path[j] = current_path[j], current_path[i]
                new_distance = total_distance(current_path)
                if new_distance < current_distance:
                    current_distance = new_distance
                    improved = True
                else:
                    current_path[i], current_path[j] = current_path[j], current_path[i]
    return current_path

def simulated_annealing_tsp(nodes, initial_temperature, cooling_rate, iterations):
    current_path = nodes.copy()
    best_path = current_path.copy()
    current_distance = total_distance(current_path)
    best_distance = current_distance

    for i in range(iterations):
        temperature = initial_temperature / (1 + cooling_rate * i)
        random_index1 = random.randint(0, len(nodes) - 1)
        random_index2 = random.randint(0, len(nodes) - 1)
        current_path[random_index1], current_path[random_index2] = current_path[random_index2], current_path[random_index1]

        new_distance = total_distance(current_path)
        delta = new_distance - current_distance

        if delta < 0 or math.exp(-delta / temperature) > random.random():
            current_distance = new_distance
            if current_distance < best_distance:
                best_path = current_path.copy()
                best_distance = current_distance
        else:
            current_path[random_index1], current_path[random_index2] = current_path[random_index2], current_path[random_index1]

    return best_path

def plot_cities(cities, title):
    x = [city.x for city in cities]
    y = [city.y for city in cities]
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def plot_route(cities, route, title):
    x = [city.x for city in cities]
    y = [city.y for city in cities]
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'bo-')
    for i, city in enumerate(route):
        if i == len(route) - 1:
            plt.plot([city.x, route[0].x], [city.y, route[0].y], 'bo-')
        else:
            plt.plot([city.x, route[i+1].x], [city.y, route[i+1].y], 'bo-')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def main():
    nodes = [
      City(60, 200), City(180, 200), City(80, 180), City(140, 180), City(20, 160),
      City(100, 160), City(200, 160), City(140, 140), City(40, 120), City(100, 120),
      # 继续添加更多节点
      City(60, 100), City(180, 100), City(80, 80), City(140, 80), City(20, 60),
      City(100, 60), City(200, 60), City(140, 40), City(40, 20), City(100, 20),
      # 添加更多节点
      City(60, 300), City(180, 300), City(80, 280), City(140, 280), City(20, 260),
      City(100, 260), City(200, 260), City(140, 240), City(40, 220), City(100, 220)
  ]

    initial_temperature = 1000
    cooling_rate = 0.003
    iterations = 10000

    # 爬山演算法
    start_time = time.time()
    shortest_path_hill_climbing = hill_climbing_tsp(nodes)
    end_time = time.time()
    print("Shortest Path (Hill Climbing):", [vars(city) for city in shortest_path_hill_climbing])
    print("Total Distance (Hill Climbing):", total_distance(shortest_path_hill_climbing))
    print("Time (Hill Climbing):", end_time - start_time, "seconds")
    plot_route(nodes, shortest_path_hill_climbing, "Shortest Path (Hill Climbing)")

    # 模擬退火算法
    start_time = time.time()
    shortest_path_simulated_annealing = simulated_annealing_tsp(nodes, initial_temperature, cooling_rate, iterations)
    end_time = time.time()
    print("Shortest Path (Simulated Annealing):", [vars(city) for city in shortest_path_simulated_annealing])
    print("Total Distance (Simulated Annealing):", total_distance(shortest_path_simulated_annealing))
    print("Time (Simulated Annealing):", end_time - start_time, "seconds")
    plot_route(nodes, shortest_path_simulated_annealing, "Shortest Path (Simulated Annealing)")

if __name__ == "__main__":
    main()
