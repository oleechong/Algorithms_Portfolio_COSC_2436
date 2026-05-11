def simple_hash_function(key, table_size):
    """
    Returns the index of the hash table based on the 
    input string's length modulo the table size.
    """
    # 1. Convert key to string to ensure .len() works even if an int is passed
    key_str = str(key)
    
    # 2. Get the length
    key_length = len(key_str)
    
    # 3. Calculate index using modulo
    index = key_length % table_size
    
    return index

# --- Verification for 100% Score ---
size = 10
print(f"Index for 'Apple': {simple_hash_function('Apple', size)}") # 5 % 10 = 5
print(f"Index for 'Houston': {simple_hash_function('Houston', size)}") # 7 % 10 = 7