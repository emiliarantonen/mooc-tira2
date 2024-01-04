import collections
import timeit

def lisää(n):
    items=collections.deque()

    for i in range(n+1):
        items.append(i)
    
    return items

def poista(items):
        while len(items)>0:
            items.popleft()

if __name__ == "__main__":
    n=10**5
    items=lisää(n)
    aika1 = timeit.timeit(lambda: lisää(n), number=1)
    print(aika1)

    aika2 = timeit.timeit(lambda: poista(items), number=1)
    print(aika2)