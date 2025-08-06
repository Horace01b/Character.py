from collections import deque

def word_ladder_length(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])  # (current_word, current_length)

    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    queue.append((new_word, length + 1))

    return 0


print(word_ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Output: 5
print(word_ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]))  # Output: 0
print(word_ladder_length("a", "c", ["a", "b", "c"]))  # Output: 2
print(word_ladder_length("a", "b", ["a", "b"]))  # Output: 1
print(word_ladder_length("abc", "xyz", ["abc", "abd", "acd", "xyz"]))  # Output: 4