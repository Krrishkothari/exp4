# Multiplication Module
# This module implements the multiplication operation for the calculator

def mul(a, b):
    """
    Multiply two numbers and return the result.
    
    Parameters:
    a (int/float): First number
    b (int/float): Second number
    
    Returns:
    int/float: Product of a and b
    """
    return a * b

# Test the function
if __name__ == "__main__":
    print("Testing Multiplication Function:")
    print(f"mul(10, 5) = {mul(10, 5)}")
    print(f"mul(100, 250) = {mul(100, 250)}")
    print(f"mul(-5, 15) = {mul(-5, 15)}")
