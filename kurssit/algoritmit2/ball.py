import sys 
maximi = sys.maxsize
from typing import List
from collections import deque


class Ball:
    def __init__(self, n: int) -> None:
        self.n = n
        self.lista = []
        self.tavanneet = False
        self.verkko = [[0]*(2*n + 2) for _ in range(2*n + 2)]



    def add_pair(self,
                a: int,
                b: int) -> None:
        
        self.verkko[a][b + self.n] = 1
        self.verkko[0][a] = 1
        self.verkko[b + self.n][-1] = 1

    def calculate(self):
        mahdollisten_parien_maara = 0        
        t = True
        self.lista = [i[:] for i in self.verkko]
        while t:
            self.tavanneet = [False]*len(self.verkko)
            ynnaa = self.bfs_algoritmi(0, len(self.verkko)-1, maximi)
            if ynnaa == 0:
                return mahdollisten_parien_maara
            mahdollisten_parien_maara += ynnaa

    def bfs_algoritmi(self, a: int, b: int, c: int) -> int:
        
        if self.tavanneet[a]: return 0
        if a == b: return c

        self.tavanneet[a] = True
        for i in range(len(self.verkko)):
            if self.lista[a][i] > 0:
                k = self.bfs_algoritmi(i, b, min(c, self.lista[a][i]))
                if k > 0:
                    self.lista[a][i] -= k
                    self.lista[i][a] += k
                    return k
        return 0

if __name__ == "__main__":
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2
