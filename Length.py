def length_of_longest_substring(s):
    char_index = {}
    max_len = 0
    start = 0

    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1  # skip the repeated character

        char_index[char] = end
        max_len = max(max_len, end - start + 1)

    return max_len

print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("bbbbb"))   # Output: 1
print(length_of_longest_substring("pwwkew"))  # Output: 3  ("wke")
print(length_of_longest_substring("abcabcbb")) # Output: 3  ("abc")
