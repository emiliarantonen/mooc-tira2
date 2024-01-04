class TrainPrices:
    def __init__(self):
        self.cities = {}
        self.nodes = []

    def add_city(self, name):
        index = len(self.nodes)
        self.cities[name] = index
        self.nodes.append(name)

        cities_copy = list(self.cities.keys())

        for city in cities_copy:
            self.cities[(name, city)] = float('inf')
            self.cities[(city, name)] = float('inf')
        self.cities[(name, name)] = 0

    def add_train(self, city1, city2, price):
        if (city1, city2) not in self.cities or price < self.cities[(city1, city2)]:
            self.cities[(city1, city2)] = price
            self.cities[(city2, city1)] = price

        n = len(self.nodes)
        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = self.cities[(self.nodes[i], self.nodes[j])]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        for i in range(n):
            for j in range(n):
                if self.cities[(self.nodes[i], self.nodes[j])] > matrix[i][j]:
                    self.cities[(self.nodes[i], self.nodes[j])] = matrix[i][j]




    def find_prices(self):
        n = len(self.nodes)
        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = self.cities[(self.nodes[i], self.nodes[j])]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        result = [[None] * (n + 1) for _ in range(n + 1)]
        result[0][0] = None


        sorted_nodes = sorted(self.nodes)

        for i in range(1, n + 1):
            result[0][i] = sorted_nodes[i - 1]
            result[i][0] = sorted_nodes[i - 1]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                result[i][j] = matrix[self.nodes.index(sorted_nodes[i - 1])][self.nodes.index(sorted_nodes[j - 1])] if matrix[self.nodes.index(sorted_nodes[i - 1])][self.nodes.index(sorted_nodes[j - 1])] != float('inf') else -1

        return result


if __name__ == "__main__":
    t = TrainPrices()

    t.add_city("Helsinki")
    t.add_city("Turku")
    t.add_city("Tampere")
    t.add_city("Oulu")

    t.add_train("Helsinki", "Tampere", 20)
    t.add_train("Helsinki", "Turku", 10)
    t.add_train("Tampere", "Turku", 50)


    print(t.find_prices())

    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]
