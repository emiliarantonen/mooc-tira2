import random
import heapq
import timeit

def algoritmi_1(lista):
    lista.sort()
    return sum(lista[:len(lista)//10])


def algoritmi_2(lista):
    heap = lista[:len(lista)//10]
    heapq.heapify(heap)
    for i in range(len(lista)//10, len(lista)):
        if lista[i] < heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, lista[i])
    return sum(heap)

if __name__ == "__main__":
    n = 10**6
    lista = [random.randint(1, 10**9) for _ in range(n)]


    aika_1 = timeit.timeit(lambda: algoritmi_1(lista), number=1)
    print(aika_1)

    aika_2 = timeit.timeit(lambda: algoritmi_2(lista), number=1)
    print(aika_2)
