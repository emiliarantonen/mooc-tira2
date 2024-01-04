def find(t):
    if not t:
        return []

    n = len(t)
    result = [1] * n
    prev_indices = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if t[i] > t[j] and result[i] < result[j] + 1:
                result[i] = result[j] + 1
                prev_indices[i] = j

    max_length = max(result)
    last_index = result.index(max_length)
    lis_sequence = []

    while last_index != -1:
        lis_sequence.insert(0, t[last_index])
        last_index = prev_indices[last_index]

    return lis_sequence

if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3]))  # [1, 2, 3]
    print(find([1, 1, 1, 1]))  # [1]
    print(find([5, 4, 3, 2, 1]))  # [5]
    print(find([4, 1, 5, 6, 3, 4, 1, 8]))  # [1, 3, 4, 8]
