class Components:
    def __init__(self, n):
        self.n = n
        self.cities = list(range(n))

    def add_road(self, a, b):
        city_a = self.find(a - 1)
        city_b =  self.find(b - 1)
        if city_a != city_b:
            self.cities[city_b] = city_a

    def count(self):
        return len(set(self.find(i) for i in range(self.n)))

    def find(self, i):
        if self.cities[i] == i:
            return i
        self.cities[i] = self.find(self.cities[i])
        return self.cities[i]

if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1,2)
    c.add_road(1,3)
    print(c.count()) # 3
    c.add_road(2,3)
    print(c.count()) # 3
    c.add_road(4,5)
    print(c.count()) # 2