class MaxSet:
    def __init__(self, n):
        self.items = list(range(n))
        self.size = [1] * n
        self.max = 1

    def find(self, i):
        while i != self.items[i]:
            i = self.items[i]
        return i

    def merge(self, a, b):
        a = self.find(a-1)
        b = self.find(b-1)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.items[b] = a
            self.size[a] += self.size[b]
            self.max = max(self.max, self.size[a])

    def get_max(self):
        return self.max



if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1,2)
    m.merge(3,4)
    m.merge(3,5)
    print(m.get_max()) # 3
    m.merge(1,5)
    print(m.get_max()) # 5