import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)

    def __contains__(self, value):
        if not self.root:
            return False

        node = self.root
        while node:
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            else:
                node = node.right

        return False
    
    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def __len__(self):
        if not self.root:
            return 0

        count = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return count

    def height(self):
        if not self.root:
            return -1

        max_height = 0
        stack = [(self.root, 0)]
        while stack:
            node, current_height = stack.pop()
            max_height = max(max_height, current_height)
            if node.left:
                stack.append((node.left, current_height + 1))
            if node.right:
                stack.append((node.right, current_height + 1))

        return max_height
    
    def prev(self, x):
        prev_value = None
        node = self.root

        while node:
            if node.value < x:
                prev_value = node.value
                node = node.right
            else:
                node = node.left

        return prev_value

    def next(self, x):
        next_value = None
        node = self.root

        while node:
            if node.value > x:
                next_value = node.value
                node = node.left
            else:
                node = node.right

        return next_value


if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(5)
    print(s.prev(5)) # 2
    print(s.prev(2)) # None
    print(s.next(1)) # 2
    print(s.next(2)) # 5
    print(s.next(5)) # None

