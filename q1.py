def swap(x, y):
    """
    Swaps the values of x and y using only x and y as variables.
    - x and y must be numeric.
    - Returns -1 if x and y are not numeric.
    - Prints the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    x, y = y, x  # Swapping values
    print("Swapped values:", x, y)

# Task 2: Invoking the function
print(swap("Apple", 10))  # Should return -1
swap(9, 17)  # Should print swapped values: 17, 9


