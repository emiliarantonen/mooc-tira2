import itertools

def count(n, k, x):
    luvut = list(range(1, n + 1))
    kombinaatiot = list(itertools.combinations(luvut, k))
    
    count = 0
    for i in kombinaatiot:
        if sum(i) == x:
            count += 1

    return count

if __name__ == "__main__":
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16