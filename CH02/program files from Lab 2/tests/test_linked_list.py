"""Lab 02: Test Cases for Linked List - Aligned with Instructions"""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from linked_list import Node, LinkedList


class TestNode:
    def test_node_creation(self):
        node = Node(42)
        assert node.data == 42
        assert node.next is None
    
    def test_node_repr(self):
        node = Node("test")
        assert repr(node) == "Node(test)"


class TestLinkedList:
    def test_empty_list(self):
        ll = LinkedList()
        assert ll.head is None
        assert len(ll) == 0
    
    def test_insert_at_head(self):
        ll = LinkedList()
        ll.insert_at_head(1)
        assert ll.head.data == 1
        assert len(ll) == 1
        
        ll.insert_at_head(2)
        assert ll.head.data == 2
        assert ll.head.next.data == 1
        assert len(ll) == 2
    
    def test_insert_at_tail(self):
        ll = LinkedList()
        ll.insert_at_tail(1)
        assert ll.head.data == 1
        
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.to_list() == [1, 2, 3]
        assert len(ll) == 3
    
    def test_delete_at_head(self):
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        
        deleted = ll.delete_at_head()
        assert deleted == 1
        assert ll.to_list() == [2, 3]
        assert len(ll) == 2
    
    def test_delete_at_head_empty(self):
        ll = LinkedList()
        deleted = ll.delete_at_head()
        assert deleted is None
    
    def test_search_found(self):
        ll = LinkedList()
        ll.insert_at_tail({"name": "Austin"})
        ll.insert_at_tail({"name": "Dallas"})
        ll.insert_at_tail({"name": "Houston"})
        
        result = ll.search("Dallas", key=lambda x: x["name"])
        assert result is not None
        assert result.data["name"] == "Dallas"
    
    def test_search_not_found(self):
        ll = LinkedList()
        ll.insert_at_tail({"name": "Austin"})
        ll.insert_at_tail({"name": "Dallas"})
        
        result = ll.search("Chicago", key=lambda x: x["name"])
        assert result is None
    
    def test_to_list(self):
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.to_list() == [1, 2, 3]
    
    def test_to_list_empty(self):
        ll = LinkedList()
        assert ll.to_list() == []
    
    def test_repr(self):
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        assert repr(ll) == "LinkedList([1, 2])"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
