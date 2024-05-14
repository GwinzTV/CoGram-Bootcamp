# Trees
'''
COMPONENTS OF THE NODE:
Nodes: Data elements in the tree
Edges: Connections between nodes
Root: The topmost node in the tree
Leaves: Nodes without child nodes
Depth: Number of edges from the root to a node
Height: Maximum depth of the tree

PROPERTIES OF TREES
 - Each node (except the root) has exactly one parent node
 - There is a unique path from the root to each node
 - The tree is *acyclic* (no cycles)
 - Trees are recursive data structures:
  - Each node can be treated as the root of a subtree
'''
# Binary search Tree
'''
A Binary tree is a tree in which each node has at most two child nodes
(left and right)

PROPERTIES:
 - the left subtree of a node contains only nodes with keys less than
   the node's key
 - the right subtree of a ndoe contains only nodes with keys greater
   than the node's key
 - both the left and right subtrees must also be binary search trees
'''
# AVL Trees
'''
An AVL tree is a self-balancing binary search tree
 - The heights of the left and right subtrees of any node differs
   by at most one.

 - this property ensures that the tree remains balanced,
   preventing degeneration into a linked list.

Efficient searching and sorting (since the tree is balanced)
'''
# Heap Data Structure
'''

'''
