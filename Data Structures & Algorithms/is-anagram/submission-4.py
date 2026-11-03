class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = dict()
        count_t = dict()
        for i, j in zip(s,t):
            if i not in count_s:
                count_s[i] = 1
            else:
                count_s[i] += 1
            if j not in count_t:
                count_t[j] = 1
            else:
                count_t[j] += 1
        return count_s == count_t