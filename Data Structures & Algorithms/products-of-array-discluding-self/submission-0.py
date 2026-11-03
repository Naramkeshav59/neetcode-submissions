class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefixes = [1]
        suffixes = [1]
        i = 0
        while i < len(nums) - 1:
            prefixes.append(prefixes[-1] * nums[i])
            suffixes.append(suffixes[-1] * nums[-1-i])
            i = i + 1
        
        for idx in range(len(nums)):
            result.append(prefixes[idx] * suffixes[-1-idx])
        return result

        