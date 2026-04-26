class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        subset = set()
        maxCount = 0

        for right in range(len(s)):
            while s[right] in subset:
                subset.remove(s[left])
                left += 1

            subset.add(s[right])
            maxCount = max(maxCount, len(subset))

        return maxCount 
