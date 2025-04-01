  def find_and_replace(lst, find_val, replace_val):

  """
    Searches for all occurrences of a value (find_val) in a given list (lst) 
    and replaces them with another value (replace_val).
    - lst must be a list.
    - Returns the modified list.
    """
    if not isinstance(lst, list):
        return "Error: lst must be a list"
    
    return [replace_val if item == find_val else item for item in lst]

# Task 2: Invoking the function
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)) 
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))  

