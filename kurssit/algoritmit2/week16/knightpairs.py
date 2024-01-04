class MaximumThreateningPairs:
    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)
        self.cols = len(graph[0])

    def is_threatened(self, x, y, i, j):
        return (abs(x - i) == 2 and abs(y - j) == 1) or (abs(x - i) == 1 and abs(y - j) == 2)

    def bpm(self, u, matchR, seen):
        for v in range(self.cols):
            if self.graph[u][v] and not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False

    def threatening_pairs(self):
        matchR = [-1] * self.cols
        count = 0
        for i in range(self.rows):
            seen = [False] * self.cols
            if self.bpm(i, matchR, seen):
                count += 1
        return count//2

def construct_graph(board):
    rows = len(board)
    cols = len(board[0])
    graph = [[0 for _ in range(rows * cols)] for _ in range(rows * cols)]

    threatening_knights = MaximumThreateningPairs(graph)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '*':
                for x in range(rows):
                    for y in range(cols):
                        if board[x][y] == '*' and threatening_knights.is_threatened(x, y, i, j):
                            graph[(x * cols) + y][(i * cols) + j] = 1

    return graph


def count(graph):
    knights = construct_graph(graph)
    threatening_knights = MaximumThreateningPairs(knights)
    return threatening_knights.threatening_pairs()



if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(count(r)) # 3
