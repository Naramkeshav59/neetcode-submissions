class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in store:
                store[key] = []
            store[key].append(i)
        return [i for i in store.values()]