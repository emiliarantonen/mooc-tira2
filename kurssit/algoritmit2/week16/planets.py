import sys
inf = sys.maxsize
from copy import deepcopy
from collections import deque

class Planets:
    def __init__(self,n): 
        self.n = n+1
        self.muisti = []
        self.yhdistetyt = [[-1 for i in range(self.n)] for j in range(self.n)]
        self.vierailtu = [False for i in range(self.n)] # Ollaanko käyty läpi

    def add_teleport(self, a, b):
        if self.yhdistetyt[a][b] == -1:
            self.yhdistetyt[a][b] = 0
        self.yhdistetyt[a][b] += 1
        self.yhdistetyt[b][a] = max(0, self.yhdistetyt[b][a])
    
    def calculate(self):
        perittavat = [-1]*self.n
        pisin_reitti = 0
        self.muisti = deepcopy(self.yhdistetyt)                                            
        while self.bfs_algoritmi(1, self.n, perittavat):
            kasiteltava_reitti = inf
            alkio = self.n - 1
            while not alkio == 1: 
                perittava = perittavat[alkio]
                kasiteltava_reitti = min(kasiteltava_reitti, self.muisti[perittava][alkio])
                alkio = perittava

            alkio = self.n - 1
            while not alkio == 1:
                perittava = perittavat[alkio]
                self.muisti[perittava][alkio] -= kasiteltava_reitti
                self.muisti[alkio][perittava] += kasiteltava_reitti
                alkio = perittava
            pisin_reitti += kasiteltava_reitti
        return pisin_reitti
    
    def bfs_algoritmi(self, start, pysayta, perittavat):
        pysayta -= 1
        self.vierailtu = [False for i in range(self.n)]
        self.vierailtu[start] = True
        varasto = deque()
        varasto.append(start)
        while varasto:
            uusi_alkio = varasto.popleft()
            viereinens = self.muisti[uusi_alkio]
            for i, viereinen in enumerate(viereinens):
                if self.vierailtu[i] <= 0: 
                    if viereinen > 0:
                        varasto.append(i)
                        perittavat[i] = uusi_alkio
                        self.vierailtu[i] = True
                        if i == pysayta:
                            return True
        return False  
    
if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1,2)
    p.add_teleport(2,5)
    print(p.calculate()) # 1
    p.add_teleport(1,5)
    print(p.calculate()) # 2