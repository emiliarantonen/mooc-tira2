class UnionFind:
    def __init__(self, n):
        self.link = {node: None for node in range(1, n + 1)}
        self.size = {node: 1 for node in range(1, n + 1)}
            
    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
 
        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]   
class Kruskal:
    def __init__(self, n):
        self.n = n
        self.edges = []
        
    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))
        
    def construct(self):
        self.edges.sort(key=lambda x: x[2])

        uf = UnionFind(self.n)
        edges_count = 0
        tree_weight = 0

        for edge in self.edges:
            node_a, node_b, weight = edge
            if uf.find(node_a) != uf.find(node_b):
                uf.union(node_a, node_b)
                edges_count += 1
                tree_weight += weight
        
        if edges_count != self.n - 1:
            return None


        return tree_weight

if __name__ == "__main__":
    k = Kruskal(1000)

    for i in range(1, 1000):
        for j in range(i + 1, 1001):  # Ensures that j > i to avoid duplicate edges
            k.add_edge(i, j, min(i, j))


    print(k.construct())