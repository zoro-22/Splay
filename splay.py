class SplayTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(new_node, self.root)

    def _insert(self, new_node, current_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(new_node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(new_node, current_node.right)
        self._splay(new_node)

    def _splay(self, node):
        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent

            if grandparent is None:
                self._rotate(node, parent)
            elif parent.left == node:
                self._zig(node, parent, grandparent)
            else:
                self._zag(node, parent, grandparent)

    def _zig(self, node, parent, grandparent):
        grandparent.left = node.right
        if node.right is not None:
            node.right.parent = grandparent

        node.parent = grandparent.parent
        if grandparent.parent is not None:
            if grandparent.parent.left == grandparent:
                grandparent.parent.left = node
            else:
                grandparent.parent.right = node

        grandparent.right = node
        node.right = parent
        parent.parent = node

    def _zag(self, node, parent, grandparent):
        grandparent.right = node.left
        if node.left is not None:
            node.left.parent = grandparent

        node.parent = grandparent.parent
        if grandparent.parent is not None:
            if grandparent.parent.left == grandparent:
                grandparent.parent.left = node
            else:
                grandparent.parent.right = node

        grandparent.left = node
        node.left = parent
        parent.parent = node

    def inorder(self):
        def _inorder(node):
            if node is None:
                return

            _inorder(node.left)
            print(node.value)
            _inorder(node.right)

        _inorder(self.root)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

if __name__ == "__main__":
    tree = SplayTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.inorder()  # Prints 5, 10, 15
