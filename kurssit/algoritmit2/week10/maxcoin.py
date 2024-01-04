import itertools

def find(x, coins):
    result = {}

    result[0] = 0
    for s in range(1, x + 1):
        result[s] = float("-inf")
        for coin in coins:
            if s - coin >= 0:
                new_result = result[s - coin] + 1
                if new_result > result[s]:
                    result[s] = new_result

    count = result[x]
    return count if count != float("-inf") else -1

if __name__ == "__main__":
    print(find(13, [1, 2, 5])) # 13
    print(find(13, [2, 3, 5])) # 6
    print(find(13, [2, 4, 6])) # -1
    print(find(42, [8, 9, 11, 15])) # 5