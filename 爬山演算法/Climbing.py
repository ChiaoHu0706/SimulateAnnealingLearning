import numpy as np
import matplotlib.pyplot as plt
import time

def euclidean_distance(point1, point2):
    """計算兩點之間的歐氏距離"""
    return np.linalg.norm(point1 - point2)

def total_distance(points, order):
    """計算路徑的總距離"""
    distance = 0
    for i in range(len(order) - 1):
        distance += euclidean_distance(points[order[i]], points[order[i+1]])
    distance += euclidean_distance(points[order[-1]], points[order[0]])  # 回到起點
    return distance

def climb_hill(points):
    """爬山演算法求解TSP"""
    num_cities = len(points)
    order = np.arange(num_cities)  # 初始路徑順序
    np.random.shuffle(order)  # 隨機初始化路徑順序

    best_order = order.copy()
    best_distance = total_distance(points, best_order)
    start_time = time.time()

    while True:
        improved = False
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                new_order = best_order.copy()
                new_order[i], new_order[j] = new_order[j], new_order[i]  # 交換兩個城市的位置
                new_distance = total_distance(points, new_order)
                if new_distance < best_distance:
                    best_order = new_order
                    best_distance = new_distance
                    improved = True
        if not improved:
            break

    end_time = time.time()
    execution_time = end_time - start_time

    return best_order, best_distance, execution_time

# 定義城市坐標
points = np.array([
    [60, 200], [180, 200], [80, 180], [140, 180],
    [20, 160], [100, 160], [200, 160], [140, 140],
    [40, 120], [100, 120]
])

# 使用爬山演算法求解TSP
best_order, best_distance, execution_time = climb_hill(points)

# 顯示結果
print("最佳路徑順序:", best_order)
print("最佳路徑總距離:", best_distance)
print("計算時間:", execution_time, "秒")

# 繪製路徑圖表
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], c='blue', label='Cities')
for i in range(len(best_order) - 1):
    plt.plot([points[best_order[i]][0], points[best_order[i+1]][0]],
             [points[best_order[i]][1], points[best_order[i+1]][1]],
             c='red', linewidth=1)
plt.plot([points[best_order[-1]][0], points[best_order[0]][0]],
         [points[best_order[-1]][1], points[best_order[0]][1]],
         c='red', linewidth=1, label='Best Path')
plt.scatter(points[best_order[0]][0], points[best_order[0]][1], c='green', label='Start/End')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Traveling Salesman Problem - Hill Climbing')
plt.legend()
plt.grid(True)
plt.show()