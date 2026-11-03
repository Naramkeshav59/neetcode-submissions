class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1

            while left < right:
                total = nums[idx] + nums[left] + nums[right]

                if total == 0:
                    triplet = (nums[idx], nums[left], nums[right])
                    result.add(triplet)

                    left += 1
                    right -= 1

                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in result]
