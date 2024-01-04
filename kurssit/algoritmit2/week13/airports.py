class Airports:

    def __init__(self,n):
        self.n = n + 1
        self.lentokentta = [[] for _ in range(self.n)]


    def add_link(self,a,b):
        self.lentokentta[a].append(b)

  
    def check(self):
        yhtenaisyys = True
        for i in range(1, self.n):
            visited = [False]*self.n
            self.kenttien_lapikaynti(i, visited)
            yhtenaisyys = yhtenaisyys and False not in visited[1:]
        return yhtenaisyys


    def kenttien_lapikaynti(self, i, visited):
        if visited[i] == True: return
        visited[i] = True
        for i in self.lentokentta[i]:
            self.kenttien_lapikaynti(i, visited)
            
if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1, 2)
    a.add_link(2, 3)
    a.add_link(1, 3)
    a.add_link(4, 5)
    print(a.check()) # False
    a.add_link(3, 5)
    a.add_link(1, 4)
    print(a.check()) # False
    a.add_link(5, 1)
    print(a.check()) # True