class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        for i, j in zip(s,t):
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 0
            if j in t_dict:
                t_dict[j] += 1
            else:
                t_dict[j] = 0
        return (s_dict == t_dict) and len(s) == len(t)
            