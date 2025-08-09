"""
Module: binary_search_tree - unbalanced.
License: MIT
Author: Prashant Garg
Date: 2025-08-09

Description:
------------
This module provides an implementation of a Binary Search Tree (BST) in Python.
It includes the Node class to represent each node in the tree and the 
BinarySearchTree class to manage the tree operations such as insertion, 
searching, removal, and traversal.
"""


class Node:
    """
    A class representing a node in a binary search tree.

    Attributes:
    ----------
    value : int
        The value stored in the node.
    left : Node, optional
        A reference to the left child node.
    right : Node, optional
        A reference to the right child node.
    """

    def __init__(self, value: int):
        self.value = value
        self.left: Node = None
        self.right: Node = None


class BinarySearchTree:
    """
    A class representing a binary search tree.

    Attributes:
    ----------
    root : Node, optional
        The root node of the binary search tree.

    Methods:
    -------
    insert(value: int) -> bool
        Inserts a value into the binary search tree.
    contains(value: int) -> bool
        Checks if a value exists in the binary search tree.
    remove(value: int) -> bool
        Removes a value from the binary search tree.
    __str__() -> str
        Returns a string representation of the binary search tree.
    _in_order_traversal(node: Node, values: list)
        Performs an in-order traversal of the tree and appends node values to the list.
    _print_tree(node: Node, prefix: str, is_left: bool)
        Recursively prints the tree structure.
    """

    def __init__(self):
        self.root: Node = None

    def insert(self, value: int) -> bool:
        """
        Inserts a value into the binary search tree.

        Parameters:
        ----------
        value : int
            The value to be inserted into the tree.

        Returns:
        -------
        bool
            True if the value was inserted, False if the value already exists in the tree.
        """
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True

        current_node: Node = self.root
        while True:
            if new_node.value == current_node.value:
                return False
            elif new_node.value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    return True
                current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = new_node
                    return True
                current_node = current_node.left

    def contains(self, value: int) -> bool:
        """
        Checks if a value exists in the binary search tree.

        Parameters:
        ----------
        value : int
            The value to search for in the tree.

        Returns:
        -------
        bool
            True if the value exists in the tree, False otherwise.
        """
        temp: Node = self.root
        while temp is not None:
            if value == temp.value:
                return True
            elif value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return False

    def remove(self, value: int) -> bool:
        """
        Removes a value from the binary search tree.

        Parameters:
        ----------
        value : int
            The value to be removed from the tree.

        Returns:
        -------
        bool
            True if the value was removed, False if the value does not exist in the tree.
        """

        def _remove_node(node: Node, value: int) -> Node:
            if node is None:
                return None
            if value < node.value:
                node.left = _remove_node(node.left, value)
            elif value > node.value:
                node.right = _remove_node(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self._find_min(node.right)
                node.value = temp.value
                node.right = _remove_node(node.right, temp.value)
            return node

        if not self.contains(value):
            return False
        self.root = _remove_node(self.root, value)
        return True

    def _find_min(self, node: Node) -> Node:
        """
        Finds the node with the minimum value in the tree.

        Parameters:
        ----------
        node : Node
            The node to start the search from.

        Returns:
        -------
        Node
            The node with the minimum value.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current


def main():
    """
    The main function to demonstrate the usage of the BinarySearchTree class.
    """
    bst = BinarySearchTree()
    for value in [10, 23, 4, 56, 73, 33, 44, 38]:
        bst.insert(value)

    print(bst.contains(33))
    print(bst.contains(100))
    bst.remove(33)
    print(bst.contains(33))


if __name__ == "__main__":
    main()
