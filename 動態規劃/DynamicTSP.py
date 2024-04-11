#動態規劃
import math

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(city1, city2):
    return math.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)

def tsp(nodes):
    n = len(nodes)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    path = [[-1] * n for _ in range(1 << n)]

    # Base case: if there's only one node
    dp[1][0] = 0

    for mask in range(1, 1 << n):
        for i in range(n):
            if mask & (1 << i):
                for j in range(n):
                    if mask & (1 << j):
                        if dp[mask ^ (1 << i)][j] + distance(nodes[j], nodes[i]) < dp[mask][i]:
                            dp[mask][i] = dp[mask ^ (1 << i)][j] + distance(nodes[j], nodes[i])
                            path[mask][i] = j

    min_distance = float('inf')
    last_node = -1
    for i in range(n):
        if dp[(1 << n) - 1][i] + distance(nodes[i], nodes[0]) < min_distance:
            min_distance = dp[(1 << n) - 1][i] + distance(nodes[i], nodes[0])
            last_node = i

    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                print(i, end=' ')
        print("Distance:", dp[mask][last_node] + distance(nodes[last_node], nodes[0]), "Current Best Distance:", min_distance)

    return min_distance

if __name__ == "__main__":
    nodes = [
        City(60, 200), City(180, 200), City(80, 180), City(140, 180), City(20, 160),
        City(100, 160), City(200, 160), City(140, 140), City(40, 120), City(100, 120)
    ]

    min_distance = tsp(nodes)
    print("Minimum Distance:", min_distance)
