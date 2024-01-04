from math import inf
from collections import deque

class Download:
    def __init__(self,n):
        self.n = n+1
        self.yhteys = [[0]*self.n for i in range(self.n)]
        self.verkko = [[] for j in range(self.n)]

    def add_link(self,a,b,x):
        self.verkko[a].append(b)
        self.yhteys[a][b] = self.yhteys[a][b] + x

    def calculate(self,a,b):
        t = True
        verkon_lista = [[0]*self.n for k in range(self.n)]
        tulos = 0
        while t:
            l, v = self.bfs_algoritmi(a, b, verkon_lista)
            if l == 0: return tulos
            tulos += l
            j = b
            while not j == a:
                i = v[j]
                verkon_lista[i][j] += l
                verkon_lista[j][i] -= l
                j = i

    def bfs_algoritmi(self, a, b, verkon_lista):
        jono = deque()
        perittava = [-1]*self.n
        t = [inf]*self.n
        jono.append(a)
        while len(jono) != 0:
            alkio = jono.popleft()
            for i in self.verkko[alkio]:
                if self.yhteys[alkio][i] - verkon_lista[alkio][i] > 0:
                    if perittava[i] == -1:
                        perittava[i] = alkio
                        t[i] = min(t[alkio], self.yhteys[alkio][i] - verkon_lista[alkio][i])
                        if i == b: return t[b], perittava
                        jono.append(i)
        return 0, perittava

if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1, 4)) # 0
    d.add_link(1, 2, 5)
    d.add_link(2, 4, 6)
    d.add_link(1, 4, 2)
    print(d.calculate(1, 4)) # 7
    d.add_link(1, 3, 4)
    d.add_link(3, 2, 2)
    print(d.calculate(1, 4)) # 8