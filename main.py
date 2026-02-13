# Calculator Application - Main File
# This file integrates all calculator operations

# Import functions from feature modules
from add import add
from sub import sub
from mul import mul

def main():
    """
    Main function that calls add(), sub(), and mul() functions
    from the merged feature branches.
    """
    print("Calculator Application")
    print("=" * 50)
    
    # Test values
    num1 = 10
    num2 = 5
    
    # Addition operation
    result_add = add(num1, num2)
    print(f"\nAddition: {num1} + {num2} = {result_add}")
    
    # Subtraction operation
    result_sub = sub(num1, num2)
    print(f"Subtraction: {num1} - {num2} = {result_sub}")
    
    # Multiplication operation
    result_mul = mul(num1, num2)
    print(f"Multiplication: {num1} * {num2} = {result_mul}")
    
    print("\n" + "=" * 50)
    print("All operations completed successfully!")
    print("All feature branches have been integrated.")

if __name__ == "__main__":
    main()
