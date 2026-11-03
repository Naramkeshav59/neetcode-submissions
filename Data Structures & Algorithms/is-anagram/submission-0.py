class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        t_counts, s_counts = dict(), dict()
        for idx in range(len(s)):
            if s[idx] not in s_counts:
                s_counts[s[idx]] = 0
            else:
                s_counts[s[idx]] = s_counts[s[idx]] + 1
            if t[idx] not in t_counts:
                t_counts[t[idx]] = 0
            else:
                t_counts[t[idx]] = t_counts[t[idx]] + 1

        return (s_counts == t_counts)

        