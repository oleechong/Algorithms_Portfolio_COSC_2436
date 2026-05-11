"""Lab 02: Test Cases for Selection Sort - Aligned with Instructions"""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sort import find_smallest_index, selection_sort, python_builtin_sort


class TestFindSmallestIndex:
    """Tests for find_smallest_index as defined in instructions."""
    
    def test_find_smallest_basic(self):
        arr = [{"val": 5}, {"val": 3}, {"val": 6}, {"val": 2}, {"val": 10}]
        assert find_smallest_index(arr, key=lambda x: x["val"], start=0) == 3
    
    def test_find_smallest_first(self):
        arr = [{"val": 1}, {"val": 3}, {"val": 6}, {"val": 2}, {"val": 10}]
        assert find_smallest_index(arr, key=lambda x: x["val"], start=0) == 0
    
    def test_find_smallest_last(self):
        arr = [{"val": 5}, {"val": 3}, {"val": 6}, {"val": 2}, {"val": 1}]
        assert find_smallest_index(arr, key=lambda x: x["val"], start=0) == 4
    
    def test_find_smallest_with_start(self):
        arr = [{"val": 1}, {"val": 5}, {"val": 3}, {"val": 6}, {"val": 2}]
        assert find_smallest_index(arr, key=lambda x: x["val"], start=1) == 4
    
    def test_find_smallest_single(self):
        arr = [{"val": 42}]
        assert find_smallest_index(arr, key=lambda x: x["val"], start=0) == 0


class TestSelectionSort:
    """Tests for selection_sort as defined in instructions (key is required)."""
    
    def test_sort_basic(self):
        arr = [5, 3, 6, 2, 10]
        result = selection_sort(arr, key=lambda x: x)
        assert result == [2, 3, 5, 6, 10]
    
    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = selection_sort(arr, key=lambda x: x)
        assert result == [1, 2, 3, 4, 5]
    
    def test_sort_reverse_order(self):
        arr = [5, 4, 3, 2, 1]
        result = selection_sort(arr, key=lambda x: x)
        assert result == [1, 2, 3, 4, 5]
    
    def test_sort_empty(self):
        arr = []
        result = selection_sort(arr, key=lambda x: x)
        assert result == []
    
    def test_sort_single(self):
        arr = [42]
        result = selection_sort(arr, key=lambda x: x)
        assert result == [42]
    
    def test_sort_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = selection_sort(arr, key=lambda x: x)
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_sort_with_dict_key(self):
        """Test sorting cities by population as shown in instructions."""
        cities = [
            {"name": "Dallas", "population": 1304379},
            {"name": "Austin", "population": 978908}
        ]
        result = selection_sort(cities, key=lambda x: x["population"])
        assert result[0]["name"] == "Austin"
        assert result[1]["name"] == "Dallas"
    
    def test_sort_reverse(self):
        """Test reverse=True for descending sort."""
        cities = [
            {"name": "Austin", "population": 978908},
            {"name": "Dallas", "population": 1304379}
        ]
        result = selection_sort(cities, key=lambda x: x["population"], reverse=True)
        assert result[0]["name"] == "Dallas"
        assert result[1]["name"] == "Austin"
    
    def test_does_not_modify_original(self):
        """Instructions say: 'Create a copy to avoid modifying original'"""
        original = [5, 3, 6, 2, 10]
        copy = original.copy()
        selection_sort(original, key=lambda x: x)
        assert original == copy


class TestPythonBuiltinSort:
    """Tests for python_builtin_sort as defined in instructions."""
    
    def test_builtin_sort_basic(self):
        arr = [5, 3, 6, 2, 10]
        result = python_builtin_sort(arr, key=lambda x: x)
        assert result == [2, 3, 5, 6, 10]
    
    def test_builtin_sort_with_key(self):
        cities = [
            {"name": "Dallas", "population": 1304379},
            {"name": "Austin", "population": 978908}
        ]
        result = python_builtin_sort(cities, key=lambda x: x["population"])
        assert result[0]["name"] == "Austin"
    
    def test_builtin_sort_reverse(self):
        arr = [1, 2, 3, 4, 5]
        result = python_builtin_sort(arr, key=lambda x: x, reverse=True)
        assert result == [5, 4, 3, 2, 1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
