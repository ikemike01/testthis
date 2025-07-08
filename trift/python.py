"""
Python module for testthis project.

This module provides basic functionality for testing and experimentation.
"""


def hello_world():
    """
    Returns a simple greeting message.
    
    Returns:
        str: A greeting message
    """
    return "Hello, World! This is the testthis project."


def add_numbers(a, b):
    """
    Adds two numbers together.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
        
    Returns:
        int or float: Sum of a and b
    """
    return a + b


def get_project_info():
    """
    Returns information about the testthis project.
    
    Returns:
        dict: Project information
    """
    return {
        "name": "testthis",
        "version": "0.1.0",
        "description": "A Python project for testing and experimentation",
        "author": "testthis project"
    }


if __name__ == "__main__":
    # Example usage when run directly
    print(hello_world())
    print(f"2 + 3 = {add_numbers(2, 3)}")
    
    info = get_project_info()
    print(f"Project: {info['name']} v{info['version']}")
    print(f"Description: {info['description']}")