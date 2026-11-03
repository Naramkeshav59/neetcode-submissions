class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0, 0
        count = set()
        max_length = 0

        while r < len(s):
            if s[r] not in count:
                count.add(s[r])
                max_length = max(max_length, r - l + 1)
                r += 1
            else:
                count.remove(s[l])
                l += 1

        return max_length
