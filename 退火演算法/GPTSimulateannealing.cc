#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cstdlib>

struct City {
    int x, y;
};

// 計算兩個城市之間的距離
double distance(const City& city1, const City& city2) {
    return std::sqrt(std::pow(city1.x - city2.x, 2) + std::pow(city1.y - city2.y, 2));
}

// 計算整個路徑的總距離
double totalDistance(const std::vector<City>& path) {
    double total = 0.0;
    for (size_t i = 0; i < path.size() - 1; ++i) {
        total += distance(path[i], path[i + 1]);
    }
    total += distance(path.back(), path.front()); // 回到起點
    return total;
}

// 模擬退火算法
std::vector<City> simulatedAnnealingTSP(std::vector<City> nodes, double initialTemperature, double coolingRate, int iterations) {
    std::vector<City> currentPath = nodes;
    std::vector<City> bestPath = currentPath;
    double currentDistance = totalDistance(currentPath);
    double bestDistance = currentDistance;

    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    for (int i = 0; i < iterations; ++i) {
        double temperature = initialTemperature / (1 + coolingRate * i);
        int randomIndex1 = std::rand() % (nodes.size() - 1);
        int randomIndex2 = std::rand() % (nodes.size() - 1);
        std::swap(currentPath[randomIndex1], currentPath[randomIndex2]);
        
        double newDistance = totalDistance(currentPath);
        double delta = newDistance - currentDistance;
        
        if (delta < 0 || std::exp(-delta / temperature) > static_cast<double>(std::rand()) / RAND_MAX) {
            currentDistance = newDistance;
            if (currentDistance < bestDistance) {
                bestPath = currentPath;
                bestDistance = currentDistance;
            }
        } else {
            std::swap(currentPath[randomIndex1], currentPath[randomIndex2]);
        }
    }

    return bestPath;
}

int main() {
   /* std::vector<City> nodes = {
        {60, 200}, {180, 200}, {80, 180}, {140, 180}, {20, 160},
        {100, 160}, {200, 160}, {140, 140}, {40, 120}, {100, 120}
    };*/
 std::vector<City> nodes = {
        {60, 200}, {180, 200}, {80, 180}, {140, 180}, {20, 160},
        {100, 160}, {200, 160}, {140, 140}, {40, 120}, {100, 120},
        // 继续添加更多节点
        {60, 100}, {180, 100}, {80, 80}, {140, 80}, {20, 60},
        {100, 60}, {200, 60}, {140, 40}, {40, 20}, {100, 20},
        // 添加更多节点
        {60, 300}, {180, 300}, {80, 280}, {140, 280}, {20, 260},
        {100, 260}, {200, 260}, {140, 240}, {40, 220}, {100, 220}
    };

    double initialTemperature = 1000.0;
    double coolingRate = 0.003;
    int iterations = 10000;

    std::clock_t start = std::clock();
    std::vector<City> shortestPath = simulatedAnnealingTSP(nodes, initialTemperature, coolingRate, iterations);
    std::clock_t end = std::clock();

    std::cout << "Shortest Path:" << std::endl;
    for (const auto& city : shortestPath) {
        std::cout << "(" << city.x << ", " << city.y << ")" << std::endl;
    }
    std::cout << "Total Distance: " << totalDistance(shortestPath) << std::endl;
    std::cout << "Time: " << static_cast<double>(end - start) / CLOCKS_PER_SEC << " seconds" << std::endl;

    return 0;
}
