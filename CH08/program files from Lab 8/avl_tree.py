"""
Lab 08: Balanced Trees
Implement AVL tree from Chapter 8.

Chapter 8 covers:
- BST problems (unbalanced = O(n))
- AVL Trees (self-balancing)
- Splay Trees
- B-Trees
"""
from typing import Optional, Any, List

class AVLNode:
    """AVL tree node with height tracking."""
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1


class AVLTree:
    """Self-balancing AVL tree."""
    
    def __init__(self):
        self.root: Optional[AVLNode] = None
    
    def height(self, node: Optional[AVLNode]) -> int:
        """Get height of node (None = 0)."""
        return node.height if node else 0
    
    def balance_factor(self, node: AVLNode) -> int:
        """Calculate balance factor: height(left) - height(right)."""
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def rotate_right(self, y: AVLNode) -> AVLNode:
        """Right rotation for left-heavy tree."""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x
    
    def rotate_left(self, x: AVLNode) -> AVLNode:
        """Left rotation for right-heavy tree."""
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    def insert(self, value: Any) -> None:
        """Insert value and rebalance."""
        self.root = self._insert(self.root, value)
    
    def _insert(self, node: Optional[AVLNode], value: Any) -> AVLNode:
        """Recursive insert with rebalancing."""
        # 1. Standard BST insert
        if not node:
            return AVLNode(value)
        
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node # Duplicate values not allowed in this implementation

        # 2. Update height of ancestor node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # 3. Check balance factor
        balance = self.balance_factor(node)

        # 4. Rebalance (4 cases)
        # Case 1: Left Left (LL)
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # Case 2: Right Right (RR)
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # Case 3: Left Right (LR)
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Case 4: Right Left (RL)
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    
    def inorder(self) -> List[Any]:
        """Return sorted values."""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node: Optional[AVLNode], result: List) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

if __name__ == "__main__":
    tree = AVLTree()
    values = [10, 20, 5, 4, 15]
    for val in values:
        tree.insert(val)
    
    print("Inorder traversal of the AVL tree:", tree.inorder())