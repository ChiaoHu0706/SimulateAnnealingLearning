#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <limits>
#include <chrono>
struct City {
    int x, y;
};

double distance(const City& city1, const City& city2) {
    return std::sqrt(std::pow(city1.x - city2.x, 2) + std::pow(city1.y - city2.y, 2));
}

double tsp(const std::vector<City>& nodes) {
    int n = nodes.size();
    std::vector<std::vector<double>> dp(1 << n, std::vector<double>(n, std::numeric_limits<double>::infinity()));
    std::vector<std::vector<int>> path(1 << n, std::vector<int>(n, -1));
    
    // Base case: if there's only one node
    dp[1][0] = 0;

    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                for (int j = 0; j < n; ++j) {
                    if ((mask & (1 << j)) != 0) {
                        if (dp[mask ^ (1 << i)][j] + distance(nodes[j], nodes[i]) < dp[mask][i]) {
                            dp[mask][i] = dp[mask ^ (1 << i)][j] + distance(nodes[j], nodes[i]);
                            path[mask][i] = j;
                        }
                    }
                }
            }
        }
    }

    double min_distance = std::numeric_limits<double>::infinity();
    int last_node = -1;
    for (int i = 0; i < n; ++i) {
        if (dp[(1 << n) - 1][i] + distance(nodes[i], nodes[0]) < min_distance) {
            min_distance = dp[(1 << n) - 1][i] + distance(nodes[i], nodes[0]);
            last_node = i;
        }
    }
    
   
    for (int mask = 0; mask < (1 << n); ++mask) {
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                std::cout << i << " ";
            }
        }
        std::cout << " Distance: " << dp[mask][last_node] + distance(nodes[last_node], nodes[0])<< std::endl;
    }

    return min_distance;
}

int main() {
    std::vector<City> nodes = {
        {60, 200}, {180, 200}, {80, 180}, {140, 180}, {20, 160},
        {100, 160}, {200, 160}, {140, 140}, {40, 120}, {100, 120}
    };

    auto start = std::chrono::steady_clock::now();
    double min_distance = tsp(nodes);
  auto end = std::chrono::steady_clock::now();

    std::chrono::duration<double> elapsed_seconds = end - start;
    std::cout << "Minimum Distance: " << min_distance << std::endl;
    std::cout << "Elapsed time: " << elapsed_seconds.count() << "s\n";

    return 0;
}
