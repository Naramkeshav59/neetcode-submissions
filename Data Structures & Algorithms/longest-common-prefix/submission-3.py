class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in range(1,len(strs)):
            count = min(len(res), len(strs[i]))
            res = res[:count]
            
            while count:
                if res[:count] == strs[i][:count]:
                    res = res[:count]
                    break
                count -= 1
            if count == 0:
                res = ""

        return res