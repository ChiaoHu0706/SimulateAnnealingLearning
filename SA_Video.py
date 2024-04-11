import numpy as np
import random
import time
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation

def distance(points, order):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += np.linalg.norm(points[order[i]] - points[order[i + 1]])
    total_distance += np.linalg.norm(points[order[-1]] - points[order[0]])
    return total_distance

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    return np.exp((old_cost - new_cost) / temperature)

def simulated_annealing(points, initial_temperature=1000, cooling_rate=0.003, num_iter=2500):
    num_cities = len(points)
    current_order = list(range(num_cities))
    random.shuffle(current_order)
    current_cost = distance(points, current_order)

    best_order = current_order.copy()
    best_cost = current_cost

    temperature = initial_temperature

    start_time = time.time()

    plot_interval = 1  # 每2次迭代繪製一次圖表
    num_plots = num_iter // plot_interval

    # 建立資料夾用於儲存圖片
    output_folder = 'traveling_salesman_plots'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

    def update_plot(iteration):
        ax1.clear()
        ax1.scatter(points[:, 0], points[:, 1], c='blue', label='城市')
        order = all_orders[iteration]
        ax1.plot(points[order][:, 0], points[order][:, 1], c='red', linestyle='-', linewidth=1.5, label='最佳路徑')
        ax1.plot([points[order[-1]][0], points[order[0]][0]], [points[order[-1]][1], points[order[0]][1]], c='red', linestyle='-', linewidth=1.5)
        ax1.scatter(points[order[0]][0], points[order[0]][1], c='green', marker='o', label='起點')
        ax1.set_xlabel('x 坐標')
        ax1.set_ylabel('y 坐標')
        ax1.set_title('Best Path (Iteration: {})'.format(iteration * plot_interval))
        ax1.legend()
        ax1.grid(True)

        ax2.clear()
        ax2.plot(shortest_distances[:iteration+1], marker='o', linestyle='-', color='blue')
        ax2.set_xlabel('Iteration')
        ax2.set_ylabel('Shortest distance')
        ax2.set_title('The shortest distance changes with the iterations')
        ax2.grid(True)

    all_orders = []
    shortest_distances = []

    for iteration in range(num_iter):
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

        if iteration % plot_interval == 0:
            all_orders.append(current_order.copy())
            update_plot(len(all_orders) - 1)
            plt.savefig('{}/iteration_{}.png'.format(output_folder, iteration))

        shortest_distances.append(best_cost)  # 保存每次迭代的最短距離

    end_time = time.time()
    execution_time = end_time - start_time

    # 生成最佳路徑的動畫
    print("Generate best Path anime...")
    filenames = ['{}/iteration_{}.png'.format(output_folder, i) for i in range(num_plots)]
    animation1 = FuncAnimation(fig, update_plot, frames=num_plots, interval=200)
    animation1.save('traveling_salesman_animation.mp4', writer='ffmpeg')

    # 生成最短距離的動畫
    print("Generating anime...")
    fig2, ax2 = plt.subplots()
    ax2.plot(shortest_distances, marker='o', linestyle='-', color='blue')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Shortest distance')
    ax2.set_title('')
    ax2.grid(True)
    animation2 = FuncAnimation(fig2, lambda i: ax2.plot(shortest_distances[:i+1], marker='o', linestyle='-', color='blue'), frames=len(shortest_distances), interval=200)
    animation2.save('shortest_distance_animation.mp4', writer='ffmpeg')

    plt.close(fig)
    plt.close(fig2)

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

    # 顯示最佳路徑圖表
    plt.figure(figsize=(8, 6))
    plt.scatter(points[:, 0], points[:, 1], c='blue', label='城市')  # 繪製城市
    plt.plot(points[best_order][:, 0], points[best_order][:, 1], c='red', linestyle='-', linewidth=1.5, label='最佳路徑')  # 繪製最佳路徑
    plt.plot([points[best_order[-1]][0], points[best_order[0]][0]], [points[best_order[-1]][1], points[best_order[0]][1]], c='red', linestyle='-', linewidth=1.5)
    plt.scatter(points[best_order[0]][0], points[best_order[0]][1], c='green', marker='o', label='起點')  # 標記起點
    plt.xlabel('x 坐標')
    plt.ylabel('y 坐標')
    plt.title('旅行商問題最佳路徑')
    plt.legend()
    plt.grid(True)
    plt.show()