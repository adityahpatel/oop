"""
Just like list, stack, queue, heap is special way to store connected data, BST is a way to store data
Arrange the following list [10,20,4,30,4,1,5,6] in the form of binary search tree data structure.

Binary Search Tree (BST). Rules are:
1) Left subtree of a parent node contains only those child nodes with values less than value of parent node.
2) Right subtree of a parent node contains only those child nodes with values greater than value of parent node.
3) Left and right subtrees must also be Binary Search Trees
4) Each parent can have maximum of 2 child nodes.

Solution: Pehla do on piece of paper. Break down how human would insert notes 1 by 1 of that list according to rules above.
Ignore duplicate values, top node is called root node. Parent nodes without any child nodes are called LEAF nodes.

"""
from dataclasses import dataclass


"""
Just like list, stack, queue, heap is special way to store connected data, BST is a way to store data
Arrange the following list [10,20,4,30,4,1,5,6] in the form of binary search tree data structure.

Binary Search Tree (BST). Rules are:
1) Left subtree of a parent node contains only those child nodes with values less than value of parent node.
2) Right subtree of a parent node contains only those child nodes with values greater than value of parent node.
3) Left and right subtrees must also be Binary Search Trees
4) Each parent can have maximum of 2 child nodes.

Solution: Pehla do on piece of paper. Break down how human would insert notes 1 by 1 of that list according to rules above.
Ignore duplicate values, top node is called root node. Parent nodes without any child nodes are called LEAF nodes.

"""

class BinarySearchTree:
    def __init__(self, value):
        self.value: int = value
        self.lchild: BinarySearchTree  = None
        self.rchild: BinarySearchTree  = None

    def insert(self, data:int):
        if data < self.value:
            if self.lchild is None:
                self.lchild = BinarySearchTree(data)
            else:
                self.lchild.insert(data) 
                    
        elif data > self.value:
            if self.rchild is None:
                self.rchild = BinarySearchTree(data)
            else:
                self.rchild.insert(data)

tree = BinarySearchTree(10)
L = [20,4,30,4,1,5,6]
for i in L:
    tree.insert(i)

# testing
assert tree.lchild.rchild.rchild.value == 6
assert tree.rchild.rchild.value == 30


