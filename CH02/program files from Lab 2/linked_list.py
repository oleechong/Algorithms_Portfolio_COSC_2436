"""
Lab 2: Simple Linked List Implementation
Demonstrates linked list concepts from Chapter 2.
"""
from typing import Any, Optional


class Node:
    """A node in the linked list."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None
    
    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """
    Simple singly linked list.
    
    Insert: O(1) at head, O(n) at tail
    Delete: O(1) at head, O(n) elsewhere
    Search: O(n)
    Access by index: O(n)
    """
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0
    
    def insert_at_head(self, data: Any) -> None:
        """Insert at beginning - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, data: Any) -> None:
        """Insert at end - O(n)"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def delete_at_head(self) -> Optional[Any]:
        """Delete from beginning - O(1)"""
        if self.head is None:
            return None
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def search(self, target: Any, key=lambda x: x) -> Optional[Node]:
        """Search for element - O(n)"""
        current = self.head
        comparisons = 0
        
        while current:
            comparisons += 1
            if key(current.data) == target:
                print(f"LinkedList Search: Found in {comparisons} comparisons")
                return current
            current = current.next
        
        print(f"LinkedList Search: Not found after {comparisons} comparisons")
        return None
    
    def to_list(self) -> list:
        """Convert to Python list for display."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return f"LinkedList({self.to_list()})"
