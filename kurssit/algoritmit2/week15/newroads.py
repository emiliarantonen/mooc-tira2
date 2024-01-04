class NewRoads:
    def __init__(self, n):
        self.cities = n
        self.roads = []

    def add_road(self, a, b, x):
        self.roads.append((a, b, x))

    def min_cost(self):
        parent = [-1] * (self.cities + 1)

        def find(a):
            if parent[a] == -1:
                return a
            parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            a_root = find(a)
            b_root = find(b)
            if a_root != b_root:
                parent[a_root] = b_root

        self.roads.sort(key=lambda x: x[2])
        cost = 0
        connected = 0

        for road in self.roads:
            a, b, x = road
            if find(a) != find(b):
                union(a, b)
                cost += x
                connected += 1

        if connected != self.cities - 1:
            return -1

        return cost

if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1, 2, 2)
    n.add_road(1, 3, 5)
    print(n.min_cost()) # -1
    n.add_road(3, 4, 4)
    print(n.min_cost()) # 11
    n.add_road(2, 3, 1)
    print(n.min_cost()) # 7