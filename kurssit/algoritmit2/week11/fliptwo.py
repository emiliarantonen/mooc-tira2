from collections import deque

def solve(n, k):
    queue = deque(range(1, n+1))
    for i in range(k):
        if len(queue) == 1:
            return queue[0]
        a = queue.popleft()
        b = queue.popleft()
        queue.append(b)
        queue.append(a)

    return queue[0]


if __name__ == "__main__":
    print(solve(4, 3)) # 4
    print(solve(12, 5)) # 11
    print(solve(99, 555)) # 11
    print(solve(12345, 54321)) # 9875