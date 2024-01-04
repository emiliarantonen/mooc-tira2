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

if __name__ == "__main__":
    s = TreeSet()
    print(len(s)) # 0
    s.add(1)
    print(len(s)) # 1
    s.add(2)
    print(len(s)) # 2
    s.add(3)
    print(len(s)) # 3
    s.add(2)
    print(len(s)) # 3