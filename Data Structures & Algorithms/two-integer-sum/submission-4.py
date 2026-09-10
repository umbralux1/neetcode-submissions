class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for j, w in enumerate(nums[i+1:]):
                if target - v == w:
                    return [i, i + j + 1]