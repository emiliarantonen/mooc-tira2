def count(t):
    n = len(t)
    count = [1] * n

    for i in range(1, n):
        for j in range(i):
            if t[i] > t[j]:  
                count[i] += count[j]

    return sum(count)

# Testit
print(count([1, 1, 2, 2, 3, 3]))  # 26
print(count([1, 1, 1, 1]))  # 4
print(count([5, 4, 3, 2, 1]))  # 5
print(count([4, 1, 5, 6, 3, 4, 1, 8]))  # 37
