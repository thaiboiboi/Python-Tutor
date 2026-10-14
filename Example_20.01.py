class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert_from_node(self, node, number):
        if number < node.value:
            if node.left is None:
                node.left = Node(number)
            else:
                self.insert_from_node(node.left, number)
        else:
            if node.right is None:
                node.right = Node(number)
            else:
                self.insert_from_node(node.right, number)

    def insert(self, number):
        self.size += 1
        if self.root is None:
            self.root = Node(number)
        else:
            self.insert_from_node(self.root, number)

    def insert_list(self, lst):
        for number in lst:
            self.insert(number)

    def print_tree_from_node(self, node):
        if node is not None:
            self.print_tree_from_node(node.left)
            print(node.value, end=" ")
            self.print_tree_from_node(node.right)

    def print_tree(self):
        self.print_tree_from_node(self.root)

lst = [7, 2, 5, 8, 10, 4, 6, 1, 3, 9]
tree = Tree()
tree.insert_list(lst)
tree.print_tree()
print()
print("The tree contains %d nodes" % tree.size)
