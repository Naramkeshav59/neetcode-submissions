class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = dict()
        for idx ,num in enumerate(nums):
            if num not in hashMap:
                hashMap[target - num] = idx
            else:
                return [hashMap[num], idx]