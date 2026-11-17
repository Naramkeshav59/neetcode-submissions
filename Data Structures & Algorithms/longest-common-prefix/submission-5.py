class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestStr = strs[0]
        for idx, string in enumerate(strs):
            if len(string) < len(shortestStr):
                shortestStr = string
        def lcp(word: str, mini: str) -> int:
            for i in range(len(mini)):
                if word[i] != mini[i]:
                    return i
            return len(mini)

        lcp_len = len(shortestStr)
        for string in strs:
            if string != shortestStr:
                lcp_len = min(lcp_len, lcp(string, shortestStr))
        return shortestStr[0:lcp_len]

        