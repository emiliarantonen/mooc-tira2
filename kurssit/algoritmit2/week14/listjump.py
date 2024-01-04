import math
from heapq import heappush, heappop

class BestRoute:
    def __init__(self,n):
        self._items = [[] for _ in range(n)]
        self._n = n

    def add_jump(self,a,b,x):
        self._items[a].append((b, x))

    def find_route(self,a,b):
        heap = []
        kasitelty = [False]*self._n
        distance = [math.inf]*self._n
        distance[a] = 0
        heappush(heap, (0, a))
        while len(heap) != 0:
            solmu = heappop(heap)[1]
            if kasitelty[solmu]:
                continue
            kasitelty[solmu] = True
            for kaari in self._items[solmu]:
                current = distance[kaari[0]]
                new = distance[solmu] + kaari[1]
                if new < current:
                    distance[kaari[0]] = new
                    heappush(heap, (new, kaari[0]))
        return distance[b] if math.isfinite(distance[b]) else -1

def calculate(t):
    r = BestRoute(len(t))
    for i in range(len(t)):
        l = t[i]
        if i - l >= 0:
            r.add_jump(i, i - l, l)
        if i + l < len(t):
            r.add_jump(i, i + l, l)
    return r.find_route(0, len(t) - 1)

if __name__ == "__main__":
    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32