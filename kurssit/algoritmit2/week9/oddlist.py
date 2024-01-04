import itertools

def count(n, x):
    items = list(range(1, n + 1))
    count=0


    for order in itertools.permutations(items):
        if valid(order, x):
            count += 1
    
    return count

def valid(order, x):
    sums = []

    for i in range(len(order) - 1):
        sum = order[i] + order[i+1]
        if sum in sums or order[i] == x:
            return False
        sums.append(sum)
    return True


if __name__ == "__main__":
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(8, 5)) # 830