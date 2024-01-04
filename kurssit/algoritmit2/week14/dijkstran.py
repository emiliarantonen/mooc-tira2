import heapq
import random
import time

class Dijkstra:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in range(1, n + 1)}
        
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        
    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        queue = []
        heapq.heappush(queue, (0, start_node))
        
        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)
                    
        return distances


if __name__ == "__main__":
    n=5000
    d=Dijkstra(n)

    for i in range(1, n + 1):
        for j in range(i + 1, min(i + 10, n + 1)):
            weight = random.randint(1, 1000)
            d.add_edge(i, j, weight)

    start = time.time()
    distances = d.find_distances(1)
    end = time.time()

    print(end - start)
    