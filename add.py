# Addition Module
# This module implements the addition operation for the calculator

def add(a, b):
    """
    Add two numbers and return the result.
    
    Parameters:
    a (int/float): First number
    b (int/float): Second number
    
    Returns:
    int/float: Sum of a and b
    """
    return a + b

# Test the function
if __name__ == "__main__":
    print("Testing Addition Function:")
    print(f"add(10, 5) = {add(10, 5)}")
    print(f"add(100, 250) = {add(100, 250)}")
    print(f"add(-5, 15) = {add(-5, 15)}")
