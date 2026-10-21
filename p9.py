#Name: Vishvrajsinh zala
#Eno : 92600584082
#9. Write a program to solve travelling salesman problem

from itertools import permutations

# 2D distance matrix
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = ['A', 'B', 'C', 'D']
n = len(dist)

min_cost = float('inf')
best_path = ()

for path in permutations(range(1, n)):
    cost = 0
    current = 0
    
    for city in path:
        cost += dist[current][city]
        current = city

    cost += dist[current][0]
    
    if cost < min_cost:
        min_cost = cost
        best_path = (0,) + path + (0,)

route = [cities[i] for i in best_path]

print("shortest path:", " -> ".join(route))
print("minimum cost:", min_cost)
