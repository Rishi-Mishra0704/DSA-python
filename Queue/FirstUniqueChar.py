from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Initialize a dictionary to store character counts
        char_count = {}
    
        # Initialize a queue to keep track of the order of characters
        char_queue = deque()
    
        # Iterate through the string to count characters and build the queue
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            char_queue.append(char)
    
        # Iterate through the queue to find the first non-repeating character
        while char_queue:
            char = char_queue.popleft()
            if char_count[char] == 1:
                return s.index(char)
    
        # If no non-repeating character is found, return -1
        return -1

# Test cases
solution = Solution()
print(solution.firstUniqChar("leetcode"))      # Output: 0
print(solution.firstUniqChar("loveleetcode"))  # Output: 2
print(solution.firstUniqChar("aabb"))          # Output: -1
