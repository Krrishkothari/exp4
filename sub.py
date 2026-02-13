# Subtraction Module
# This module implements the subtraction operation for the calculator

def sub(a, b):
    """
    Subtract b from a and return the result.
    
    Parameters:
    a (int/float): First number (minuend)
    b (int/float): Second number (subtrahend)
    
    Returns:
    int/float: Difference of a and b
    """
    return a - b

# Test the function
if __name__ == "__main__":
    print("Testing Subtraction Function:")
    print(f"sub(10, 5) = {sub(10, 5)}")
    print(f"sub(100, 250) = {sub(100, 250)}")
    print(f"sub(-5, 15) = {sub(-5, 15)}")
