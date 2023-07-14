import itertools

def brute_force(target_string, password_length, characters):
    # Generate all possible combinations of characters
    combinations = itertools.product(characters, repeat=password_length)
    
    for combination in combinations:
        # Generate password string from combination
        password = ''.join(combination)
        
        # Check if password matches the target string
        if password == target_string:
            return password
    
    return None

# Example usage
target = "password"
length = 8
char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

result = brute_force(target, length, char_set)
if result:
    print("Password found:", result)
else:
    print("Password not found")