#標準退火演算法
import numpy as np
import random
import time
import matplotlib.pyplot as plt  # 引入 Matplotlib 用於繪圖

def distance(points, order):
    """
    計算給定順序的路徑總距離
    """
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += np.linalg.norm(points[order[i]] - points[order[i + 1]])
    total_distance += np.linalg.norm(points[order[-1]] - points[order[0]])
    return total_distance

def acceptance_probability(old_cost, new_cost, temperature):
    """
    接受新解的概率
    """
    if new_cost < old_cost:
        return 1.0
    return np.exp((old_cost - new_cost) / temperature)

def simulated_annealing(points, initial_temperature=1000, cooling_rate=0.003, num_iter=10000):
    """
    模擬退火算法
    """
    num_cities = len(points)
    current_order = list(range(num_cities))
    random.shuffle(current_order)
    current_cost = distance(points, current_order)

    best_order = current_order.copy()
    best_cost = current_cost

    temperature = initial_temperature

    start_time = time.time()

    for _ in range(num_iter):
        new_order = current_order.copy()
        i, j = random.sample(range(num_cities), 2)
        new_order[i], new_order[j] = new_order[j], new_order[i]

        new_cost = distance(points, new_order)

        if random.random() < acceptance_probability(current_cost, new_cost, temperature):
            current_order = new_order
            current_cost = new_cost

            if current_cost < best_cost:
                best_order = current_order.copy()
                best_cost = current_cost

        temperature *= 1 - cooling_rate

    end_time = time.time()
    execution_time = end_time - start_time

    return best_order, best_cost, execution_time

if __name__ == "__main__":
    # 使用者輸入城市的坐標
    points = np.array([
        [60, 200], [180, 200], [80, 180], [140, 180],
        [20, 160], [100, 160], [200, 160], [140, 140],
        [40, 120], [100, 120]
    ])

    # 使用退火算法找到最佳路徑
    best_order, best_cost, execution_time = simulated_annealing(points)

    # 輸出結果
    print("最佳路徑順序：", best_order)
    print("最佳路徑總距離：", best_cost)
    print("計算時間：", execution_time)

    # 繪製圖表
plt.figure(figsize=(8, 6))
plt.scatter(points[:,0], points[:,1], c='blue', label='城市')  # 繪製城市
plt.plot(points[best_order][:,0], points[best_order][:,1], c='red', linestyle='-', linewidth=1.5, label='最佳路徑')  # 繪製最佳路徑
# 加入回到起點的路線
plt.plot([points[best_order[-1]][0], points[best_order[0]][0]], [points[best_order[-1]][1], points[best_order[0]][1]], c='red', linestyle='-', linewidth=1.5)
plt.scatter(points[best_order[0]][0], points[best_order[0]][1], c='green', marker='o', label='start')  # 標記起點
plt.xlabel('x')
plt.ylabel('y')
plt.title('best Trip')
plt.legend()
plt.grid(True)
plt.show()