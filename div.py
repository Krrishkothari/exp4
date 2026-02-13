# Division Module
# This module implements the division operation for the calculator

def div(a, b):
    """
    Divide a by b and return the result.
    
    Parameters:
    a (int/float): Numerator
    b (int/float): Denominator
    
    Returns:
    float: Quotient of a and b
    
    Raises:
    ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

# Test the function
if __name__ == "__main__":
    print("Testing Division Function:")
    print(f"div(10, 5) = {div(10, 5)}")
    print(f"div(100, 4) = {div(100, 4)}")
    print(f"div(15, 3) = {div(15, 3)}")
    
    try:
        print(f"div(10, 0) = {div(10, 0)}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
