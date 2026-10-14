from random import *
from time import time

class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.sorted_list = []

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

    def sort_tree_from_node(self, node):
        if node is not None:
            self.sort_tree_from_node(node.left)
            self.sorted_list.append(node.value)
            self.sort_tree_from_node(node.right)

    def sort_tree(self):
        self.sorted_list = []
        self.sort_tree_from_node(self.root)
        return self.sorted_list

# Create a list with n arbitrary numbers:
n = 100000
#lst = [random() for i in range(n)]
lst = [10,17,9,6,5,13]
# Create the binary search tree and time the creation process:
t1 = time()
tree = Tree()
tree.insert_list(lst)
t2 = time()
t = t2 - t1
print("The construction of the binary tree takes %.3f seconds" % t)
t1 = time()
# Sort the binary search tree and time the sorting process:
list_sorted = tree.sort_tree()
t2 = time()
t = t2 - t1
print("Sorting using the binary search tree takes %.3f seconds" % t)
print("The tree contains %d nodes" % tree.size)
print("The smallest number is %.8f" % list_sorted[0])
print("The largest number is %.8f" % list_sorted[-1])
print("Verify minimum and maximum with built-in functions:")
print("The smallest number is %.8f" % min(lst))
print("The largest number is %.8f" % max(lst))
