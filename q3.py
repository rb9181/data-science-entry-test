def update_dictionary(dct, key, value):
    """
    Updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Returns the updated dictionary.
    """
    if not isinstance(dct, dict):
        return "Error: dct must be a dictionary"
    
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    dct[key] = value
    return dct

# Task 2: Invoking the function
print(update_dictionary({}, "name", "Alice"))  # Expected output: {'name': 'Alice'}
print(update_dictionary({"age": 25}, "age", 26))  # Expected output: Prints 'Original value for 'age': 25' and returns {'age': 26}
