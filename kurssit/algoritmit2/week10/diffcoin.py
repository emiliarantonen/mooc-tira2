def count(x, coins):
    result = [0] * (x + 1)
    result[0] = 1

    for coin in coins:
        for i in range(coin, x + 1):
            result[i] += result[i - coin]

    return result[x]

if __name__ == "__main__":
    print(count(5, [1])) # 1
    print(count(5, [1, 2])) # 3
    print(count(13, [1, 2, 5])) # 14
    print(count(42, [1, 5, 6, 17])) # 58
    print(count(99, [2, 4, 6])) # 0