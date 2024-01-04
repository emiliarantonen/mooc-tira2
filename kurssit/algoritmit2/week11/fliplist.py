from collections import deque

class FlipList:
    def __init__(self):
        self.__list = deque()
        self.__forward = True

    def push_last(self,x):
        if self.__forward:
            self.__list.append(x)
        else:
            self.__list.appendleft(x)


    def push_first(self,x):
        if self.__forward:
            self.__list.appendleft(x)
        else:
            self.__list.append(x)

    def pop_last(self):
        if self.__forward:
            return self.__list.pop()
        else:
            return self.__list.popleft()

    def pop_first(self):
        if self.__forward:
            return self.__list.popleft()
        else:
            return self.__list.pop()

    def flip(self):
        self.__forward = not self.__forward


if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(2)
    f.push_last(3)
    print(f.pop_first()) # 1
    f.flip()
    print(f.pop_first()) # 3