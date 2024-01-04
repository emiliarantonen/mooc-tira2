import random
import time


class BellmanFord:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.edges = []
        
    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))
        
    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        for _ in range(len(self.nodes) - 1):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    
        return distances

if __name__ == "__main__":
    n=5000
    b=BellmanFord(n)

    for i in range(1, n + 1):
        for j in range(i + 1, min(i + 10, n + 1)):
            weight = random.randint(1, 1000)
            b.add_edge(i, j, weight)

    start = time.time()
    distances = b.find_distances(1)
    end = time.time()

    print(end - start)
    
