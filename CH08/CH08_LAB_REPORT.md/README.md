## Chapter 8: Balanced Trees — Lab Report

### Student Information
- **Name:** Owen LeeChong
- **Date:** April 31, 2026

### Algorithm Analysis

#### AVL Trees
- **Balance Factor Range:** -1, 0, or 1.
- **Why rebalance?**  Rebalancing ensures the tree height remains logarithmic. Without it, a BST can degenerate into a "skewed" tree (essentially a linked list), increasing operation costs from O(log n) to O(n).
- **Time Complexity (all operations):** O(log n)

#### Rotation Cases
| Case | Imbalance                   |                     Fix                                   |
|------|-----------------------------|-----------------------------------------------------------|
| LL   | Left child's left subtree   | Single Right Rotation on the unbalanced node.             |
| RR   | Right child's right subtree | Single Left Rotation on the unbalanced node.              |
| LR   | Left child's right subtree  | Left Rotation on left child, then Right Rotation on node. |
| RL   | Right child's left subtree  | Right Rotation on right child, then Left Rotation on node.|

### Reflection Questions

1. Why is an unbalanced BST bad?
An unbalanced BST loses the efficiency that typically makes trees useful. In the worst-case scenario (inserting sorted data), a BST becomes a linear chain. This turns search, insertion, and deletion into O(n) operations, which is no better than searching through a simple list or array.

2. How do rotations maintain the BST property?
Rotations are designed to rearrange nodes while strictly adhering to the rule: Left < Root < Right. When a node is rotated, its subtrees are reattached in a way that preserves this order. For example, during a right rotation, the "middle" subtree (T2) moves from being the right child of x to the left child of y, maintaining its value relative to both.

3. What other self-balancing trees exist?
Common alternatives include Red-Black Trees (frequently used in language libraries like Java's TreeMap), Splay Trees (which move recently accessed nodes to the root), and B-Trees (highly efficient for disk storage and databases).
