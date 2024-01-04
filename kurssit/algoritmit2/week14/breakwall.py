import math
from heapq import heappush, heappop


class Labyrinth:
    def __init__(self, r):
        self._r = r
        self._m = len(r)
        self._n = len(r[0])
        for y in range(self._m):
            ax = r[y].find("A")
            if ax != -1:
                self._aloc = (ax, y)
            bx = r[y].find("B")
            if bx != -1:
                self._bloc = (bx, y)
        self._neighbours = {}
        for y in range(1, self._m - 1):
            for x in range(1, self._n - 1):
                self._neighbours[(x, y)] = []
                self._check_neighbour((x, y), (x - 1, y))
                self._check_neighbour((x, y), (x + 1, y))
                self._check_neighbour((x, y), (x, y - 1))
                self._check_neighbour((x, y), (x, y + 1))

    def _check_neighbour(self, here, neighbour):
        square = self._r[neighbour[1]][neighbour[0]]
        if square == "*":
            self._neighbours[here].append((neighbour, 1))
        if square == "." or square == "A" or square == "B":
            self._neighbours[here].append((neighbour, 0))

    def route(self):
        heap = []
        visited = dict.fromkeys(self._neighbours, False)
        distances = dict.fromkeys(self._neighbours, math.inf)
        distances[self._aloc] = 0
        heappush(heap, (0, self._aloc))
        while len(heap) != 0:
            current_vertex = heappop(heap)[1]
            if visited[current_vertex]:
                continue
            visited[current_vertex] = True
            for edge in self._neighbours[current_vertex]:
                curr = distances[edge[0]]
                new = distances[current_vertex] + edge[1]
                if new < curr:
                    distances[edge[0]] = new
                    heappush(heap, (new, edge[0]))
        return distances[self._bloc]


def count(r):
    labyrinth = Labyrinth(r)
    return labyrinth.route()


if __name__ == "__main__":
    r = [
        "########",
        "#*A*...#",
        "#.*****#",
        "#.**.**#",
        "#.*****#",
        "#..*.B.#",
        "########",
    ]
    print(count(r))  # 2