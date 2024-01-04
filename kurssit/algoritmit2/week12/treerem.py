class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

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

    def remove(self, x):
        self.root = self._remove(self.root, x)

    def _remove(self, node, x):
        if not node:
            return node

        if x < node.value:
            node.left = self._remove(node.left, x)
        elif x > node.value:
            node.right = self._remove(node.right, x)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._find_min(node.right)
            node.value = temp.value
            node.right = self._remove(node.right, temp.value)

        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(1)
    s.add(3)
    s.add(4)
    print(s)  # [1, 2, 3, 4]
    s.remove(3)
    print(s)  # [1, 2, 4]
    s.remove(2)
    print(s)  # [1, 4]
    s.remove(1)
    print(s)  # [4]
    s.remove(1)
    print(s)  # [4]
