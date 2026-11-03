class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elem = set()
        for i in nums:
            if i in elem:
                return True
            else:
                elem.add(i)
            
        return False
            