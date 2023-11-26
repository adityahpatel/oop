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

Binary Search Tree uses Recursion. Recursion means a function that calls itself in its definition.
This is super important. e.g. compute n factorial or fibonacci
"""

class BinarySearchTree:
    def __init__(self, value):
        self.value: int = value
        self.lchild: BinarySearchTree  = None
        self.rchild: BinarySearchTree  = None
        return None

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
        return None
    
    def search(self, data):
        if data == self.value:
            print('Node found')
        elif self.lchild and data < self.value:
            self.lchild.search(data)
        elif self.rchild and data > self.value:
            self.rchild.search(data)
        else:
            print('Node not found')
        return None

    def center_left_right_traversal(self):
        print(self.value)
        if self.lchild:
            self.lchild.center_left_right_traversal()
        if self.rchild:
            self.rchild.center_left_right_traversal()
        return None

    def left_center_right_traversal(self):
        if self.lchild:
            self.lchild.left_center_right_traversal()
        print(self.value)
        if self.rchild:
            self.rchild.left_center_right_traversal()
        return None

    def left_right_center_traversal(self):
        if self.lchild:
            self.lchild.left_right_center_traversal()
        if self.rchild:
            self.rchild.left_right_center_traversal()
        print (self.value)
        return None

if __name__ == "__main__":
    tree = BinarySearchTree(10)
    L = [20,4,30,4,1,5,6]
    for i in L:
        tree.insert(i)

    # testing insertion 
    assert tree.lchild.rchild.rchild.value == 6
    assert tree.rchild.rchild.value == 30
    
    # testing search function
    for i in L:
        tree.search(i)
    print ("--------------------")
    
    # Following searches should return node absent [77,80,99]:
    M = [77,80,99]
    for m in M:
        tree.search(m)
    tree = BinarySearchTree(10)
    for i in L:
        tree.insert(i)
    tree.center_left_right_traversal()

    tree = BinarySearchTree(10)
    M = [6,3,1,98,7]
    for i in M:
        tree.insert(i)
    #tree.left_center_right_traversal()
    tree.left_right_center_traversal()


