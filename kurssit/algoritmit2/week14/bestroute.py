import heapq

class BestRoute:
    def __init__(self, n):
        self.n = n
        self.bittimaa = [[] for _ in range(n)]

    def add_road(self, a, b, x):
        self.bittimaa[a-1].append((b-1, x))
        self.bittimaa[b-1].append((a-1, x))

    def find_route(self, a, b):
        length = [float('inf')] * self.n
        length[a-1] = 0
        heap = [(0, a-1)]
        while heap:
            d, u = heapq.heappop(heap)
            if length[u] < d:
                continue
            for i, j in self.bittimaa[u]:
                if length[i] > length[u] + j:
                    length[i] = length[u] + j
                    heapq.heappush(heap, (length[i], i))
        return length[b-1] if length[b-1] != float('inf') else -1


if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1, 2, 2)
    print(b.find_route(1, 3)) # -1
    b.add_road(1, 3, 5)
    print(b.find_route(1, 3)) # 5
    b.add_road(2, 3, 1)
    print(b.find_route(1, 3)) # 3