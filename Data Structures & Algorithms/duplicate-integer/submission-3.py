class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setList = set(nums)
        return len(setList) != len(nums)