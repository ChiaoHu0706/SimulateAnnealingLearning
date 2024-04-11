# TSP Problem
This is Learing Process.

Crecking -> Dynamic Programming -> Hill Climbing -> Simulated Annealing 

The Traveling Salesman Problem (TSP) is a classic problem in computer science and optimization. Given a list of cities and the distances between each pair of cities, the goal is to find the shortest possible route that visits each city exactly once and returns to the original city. In this report, we present our algorithmic approach to solving the TSP and discuss its implementation.

Algorithm Description
Our approach to solving the TSP involves implementing a heuristic algorithm known as the nearest neighbor algorithm. The algorithm starts at a random city and repeatedly selects the closest unvisited city until all cities have been visited. Once all cities have been visited, the algorithm returns to the starting city. While the nearest neighbor algorithm does not guarantee an optimal solution, it is relatively simple to implement and often produces good results, especially for large problem instances.

Implementation Details
Our implementation of the nearest neighbor algorithm is written in [programming language]. The code is organized into several modules:

Main Module: This module contains the main function that reads the input data, initializes the algorithm, and outputs the results.

Data Structures: We define data structures to represent the cities and the distances between them. This includes classes for cities and a matrix to store distance information.

Algorithm Module: This module contains the implementation of the nearest neighbor algorithm, including functions for selecting the closest unvisited city and updating the current route.
