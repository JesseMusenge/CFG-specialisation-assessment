#2.1
def count_unique_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyz"  
    unique_consonants = set()  
    
    for char in string:
        if char.lower() in consonants:
            unique_consonants.add(char.lower())
    
    return len(unique_consonants)

# Example usage
input1 = "cat"
output1 = count_unique_consonants(input1)
print(f"Input: {input1}, Output: {output1}")

input2 = "cataract"
output2 = count_unique_consonants(input2)
print(f"Input: {input2}, Output: {output2}")

"""
The time complexity of the function is O(n), where n is the length of the input string. 
This is because the function iterates over the entire string once, and each iteration takes constant time.

The space complexity of the function is O(1), where 1 is the number of unique consonants in the input string. 
This is because the function only creates a set of the unique consonants, which has a constant size.

Assumptions:
1. We assume that the operations performed within the loop, such as checking if a character is a consonant and 
adding it to the set, are constant time operations.
2. The input string is a valid string of characters
"""

#2.2
# Non-cursive solution:
def count_squares(x):
    total_squares = 0
    for i in range(1, x + 1):
        total_squares += i * 2
    return total_squares

# Tests
print(count_squares(2))  # Should output 5
print(count_squares(3))  # Should output 14

# Recursive solution:
def count_squares(x):
    if x == 1:
        return 1
    else:
        return x * 2 + count_squares(x - 1)

# Tests
print(count_squares(2)) 
print(count_squares(3))  

