""" 
A Binary Search Tree (BST) is a binary tree data structure where each node in the tree has at most two children, referred to as the left child and the right child. The key property of a Binary Search Tree is that for each node:

All nodes in the left subtree have values less than the node's value.
All nodes in the right subtree have values greater than the node's value.
This property ensures that the BST maintains a specific ordering of its elements, making it an efficient data structure for searching and retrieving data. In a well-balanced BST, the time complexity for searching, inserting, and deleting elements is O(log N), where N is the number of nodes in the tree. However, if the tree becomes unbalanced, the time complexity can degrade to O(N), which is why maintaining a balanced tree is important in practice.

Here's an example of a simple BST:

markdown
Copy code
      10
     /  \
    5   15
   / \    \
  3   7   20

            2
            /\
           1  3

"""