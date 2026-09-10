class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in prev_map:
                return [prev_map[diff], i]
            else:
                prev_map[v] = i
        