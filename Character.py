def first_non_repeating_char(s):
    # Normalize to lowercase if needed: s = s.lower()
    char_count = {}

    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    return None

print(first_non_repeating_char("Hello"))   
print(first_non_repeating_char("Swiss"))   
print(first_non_repeating_char("aabb"))    
