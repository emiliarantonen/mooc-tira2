from itertools import combinations

def create(t):
    lista=[]

    for i in range(0, len(t)+1):
        for combo in combinations(t, i):
            lista.append(sum(combo))

    lista.sort()

    return lista

if __name__ == "__main__":
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]
