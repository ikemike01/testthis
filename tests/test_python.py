"""
Tests for the trift.python module.
"""

import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from trift import python


def test_hello_world():
    """Test the hello_world function."""
    result = python.hello_world()
    assert isinstance(result, str)
    assert "Hello, World!" in result
    assert "testthis" in result


def test_add_numbers():
    """Test the add_numbers function."""
    # Test with integers
    assert python.add_numbers(2, 3) == 5
    assert python.add_numbers(0, 0) == 0
    assert python.add_numbers(-1, 1) == 0
    
    # Test with floats
    assert python.add_numbers(2.5, 3.5) == 6.0
    assert python.add_numbers(1.1, 2.2) == pytest.approx(3.3)


def test_get_project_info():
    """Test the get_project_info function."""
    info = python.get_project_info()
    
    assert isinstance(info, dict)
    assert "name" in info
    assert "version" in info
    assert "description" in info
    assert "author" in info
    
    assert info["name"] == "testthis"
    assert info["version"] == "0.1.0"
    assert isinstance(info["description"], str)
    assert isinstance(info["author"], str)


if __name__ == "__main__":
    # Run tests when executed directly
    pytest.main([__file__])