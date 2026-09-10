class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevs = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevs:
                return sorted([i, prevs[diff]])
            prevs[n] = i

