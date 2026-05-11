# solution.py

from typing import Optional, List

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data: int) -> None:
        """
        Insert data into the binary tree at the appropriate position.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current: Node, data: int) -> None:
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    def inorder_traversal(self) -> List[int]:
        """
        Perform an inorder traversal and return elements in sorted order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    def search(self, data: int) -> bool:
        """
        Search for a data value in the binary tree.
        """
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node: Optional[Node], data: int) -> bool:
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

if __name__ == "__main__":
    test_data = [7, 3, 9, 1, 5, 8, 10]
    tree = BinaryTree()
    for number in test_data:
        tree.insert(number)
    
    print(f"Inorder Traversal (Sorted): {tree.inorder_traversal()}")
    print(f"Search for 5: {tree.search(5)}")
    print(f"Search for 11: {tree.search(11)}")