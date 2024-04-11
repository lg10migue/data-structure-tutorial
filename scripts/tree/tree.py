class BinarySearchTree:
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    def __init__(self):

        # Initialize the root node.
        self.root = None

    def insert(self, key):

        # If the tree is empty, create the root node.
        if self.root is None:
            self.root = BinarySearchTree.Node(key)
        else:

            # Otherwise, insert the key into the tree.
            self._insert(self.root, key)

    def _insert(self, node, key):

        # Check if the key is less than the current node.
        if key < node.val:

            # If the left child is None, insert the key.
            if node.left is None:
                node.left = BinarySearchTree.Node(key)

            # Otherwise, recursively insert the key into the left subtree.
            else:
                self._insert(node.left, key)
        else:

            # If the right child is None, insert the key.
            if node.right is None:
                node.right = BinarySearchTree.Node(key)

            # Otherwise, recursively insert the key into the right subtree.
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):

        # If the node is None, return False.
        if node is None:
            return False

        # If the key is found, return True.
        if node.val == key:
            return True

        # Otherwise, recursively search for the key.
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):

        # If the node is None, return None.
        if node is None:
            return node

        # If the key is less than the current node, recursively delete the left key.
        if key < node.val:
            node.left = self._delete(node.left, key)

        # If the key is greater than the current node, recursively delete the right key.
        elif key > node.val:
            node.right = self._delete(node.right, key)

        # If the key is equal to the current node, delete the node.
        else:

            # If the left node has one child, return the child.
            if node.left is None:
                temp = node.right
                node = None
                return temp

            # If the right node has one child, return the child.
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # If the node has two children, find the minimum value node in the right subtree.
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return node

    def _min_value_node(self, node):

        # Find the leftmost node in the tree.
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal(self, node):

        # Perform an in-order traversal of the tree.
        result = []

        # If the node is not None, recursively traverse the left subtree, append the current node, and recursively traverse the right subtree.
        if node:
            result = self.in_order_traversal(node.left)
            result.append(node.val)
            result += self.in_order_traversal(node.right)
        return result
