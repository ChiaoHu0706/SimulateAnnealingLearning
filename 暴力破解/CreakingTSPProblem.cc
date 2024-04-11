#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <chrono>

struct City {
    int x, y;
};
double calculate_distance(const City& city1, const City& city2) {
    return std::sqrt(std::pow(city1.x - city2.x, 2) + std::pow(city1.y - city2.y, 2));
}
double total_distance(const std::vector<int>& path, const std::vector<City>& cities) {
    double total = 0;
    for (size_t i = 0; i < path.size() - 1; ++i) {
        total += calculate_distance(cities[path[i]], cities[path[i + 1]]);
    }
    total += calculate_distance(cities[path.back()], cities[path[0]]); // Return to the starting point
    return total;
}
void naive_tsp(const std::vector<City>& cities) {
    auto start_time = std::chrono::high_resolution_clock::now(); // Start time
    int num_cities = cities.size();
    double min_distance = std::numeric_limits<double>::infinity();
    std::vector<int> min_path;
  
    std::vector<int> perm(num_cities);
    for (int i = 0; i < num_cities; ++i) {
        perm[i] = i;
    }
    do {
        double distance = total_distance(perm, cities);
        if (distance < min_distance) {
            min_distance = distance;
            min_path = perm;
        }
     } 
	while (std::next_permutation(perm.begin(), perm.end()));
    auto end_time = std::chrono::high_resolution_clock::now(); // End time
    std::chrono::duration<double> execution_time = end_time - start_time; // Calculate execution time

    std::cout << "Best Path:";
    for (int city : min_path) {
        std::cout << " " << city;
    }
    std::cout << std::endl;
    std::cout << "Minimum Distance: " << min_distance << std::endl;
    std::cout << "Execution Time: " << execution_time.count() << " seconds" << std::endl;
}
int main() {
    std::vector<City> nodes = {
        {60, 200}, {180, 200}, {80, 180}, {140, 180}, {20, 160},
        {100, 160}, {200, 160}, {140, 140}, {40, 120}, {100, 120}
    };

    naive_tsp(nodes);

    return 0;
}
