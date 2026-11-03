class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = dict()
        for idx, val in enumerate(nums):
            if target - val in idx_map:
                return [idx_map[target-val], idx]
            if val not in idx_map:
                idx_map[val] = idx
             
                
