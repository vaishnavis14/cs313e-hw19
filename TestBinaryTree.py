#  File: TestBinaryTree.py

#  Description: this program adds more attributes to the tree class. These include checking if two trees are similar, finding the height
#   all nodes in a level, and num nodes in the tree

#  Student Name: Pranav Kasibhatla

#  Student UT EID: pvk249

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 11/13/22

#  Date Last Modified: 11/14/22

import sys


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lchild = lChild
        self.rchild = rChild

    def __str__(self):
        s = str(self.data)
        return s


class Tree(object):
    def __init__(self):
        self.root = None

    # Adds a given node to the tree following the BST rules
    def insert(self, data):
        new_node = Node(data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        return self.is_similar_helper(self.root, pNode.root)

    # Helper for similar. Checks node by node if each node is similar. Returns false if not similar. True otherwise
    def is_similar_helper(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif (node1 == None and node2 != None) or (node1 != None and node2 == None):
            return False
        elif node1.data != node2.data:
            return False
        else:
            return self.is_similar_helper(node1.lchild, node2.lchild) and self.is_similar_helper(node1.rchild,
                                                                                                 node2.rchild)

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        nodes = []
        if self.root == None:
            return nodes
        self.get_level_helper(level, nodes, self.root)
        return nodes

    # Helper for get_level, checks the level by checking both right subtree and left subtrees to the specified level, recursively.
    # Returns None but appends to list all nodes in a level
    def get_level_helper(self, level, nodes, node):
        if node != None:
            if level == 0:
                nodes.append(node)
            else:
                self.get_level_helper(level - 1, nodes, node.lchild)
                self.get_level_helper(level - 1, nodes, node.rchild)
                return
        if node == None:
            return []

    # Returns the height of the tree
    def get_height(self):
        if self.root == None:
            return 0
        else:
            return self.get_height_helper(self.root, 1)

    # Helper for get_height. Keeps prgressing down the tree until end is reached, keeping count of each step.
    # Returns level, which is the height of the tree
    def get_height_helper(self, node, level):
        if node != None:
            if node.rchild == None and node.lchild == None:
                return level
            if node.lchild != None and node.rchild != None:
                if self.get_height_helper(node.lchild, level + 1) > self.get_height_helper(node.rchild, level + 1):
                    return self.get_height_helper(node.lchild, level + 1)
                else:
                    return self.get_height_helper(node.rchild, level + 1)
            elif node.rchild == None:
                return self.get_height_helper(node.lchild, level + 1)
            elif node.lchild == None:
                return self.get_height_helper(node.rchild, level + 1)

                # Returns the number of nodes in the left subtree and

    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        return self.num_nodes_helper(self.root)

    # Goes through left and right child at each node. adding one to count at each level. Return the count, which is total num of nodes
    def num_nodes_helper(self, node):
        if node == None:
            return 0
        else:
            return 1 + self.num_nodes_helper(node.lchild) + self.num_nodes_helper(node.rchild)


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints
    tree1 = Tree()
    for i in tree1_input:
        tree1.insert(i)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints
    tree2 = Tree()
    for j in tree2_input:
        tree2.insert(j)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints
    tree3 = Tree()
    for k in tree3_input:
        tree3.insert(k)

    # Test your method is_similar()
    print(f"isTrue: {tree1.is_similar(tree2)}")
    print(f"isTrue: {tree2.is_similar(tree2)}")
    print(f"isTrue: {tree1.is_similar(tree1)}")
    print(f"isFalse: {tree1.is_similar(tree3)}")
    print(f"isFalse: {tree2.is_similar(tree3)}")

    # Print the various levels of two of the trees that are different
    print(f"[50]: {tree1.get_level(0)}")
    print(f"[]: {tree1.get_level(-1)}")
    print(f"[10, 40, 60, 80]: {tree1.get_level(2)}")

    # print(f"[58]: {tree3.get_level(0)}")
    print(f"[77, 65]: {tree3.get_level(1)}")
    print(f"[25, 47, 96, 80, 10, 60, 70, 40]: {tree3.get_level(2)}")

    # Get the height of the two trees that are different
    print(tree1.get_height())
    print(tree3.get_height())

    # Get the total number of nodes a binary search tree
    print(tree1.num_nodes())
    print(tree2.num_nodes())
    print(tree3.num_nodes())


if __name__ == "__main__":
    main()