class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            if self.frequency(i) not in dic.keys():
                dic[self.frequency(i)] = [i]
            else:
                dic[self.frequency(i)].append(i)
        return [i for i in dic.values()]
    def frequency(self, word):
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord('a')] += 1
        return tuple(freq)