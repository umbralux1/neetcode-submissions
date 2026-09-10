class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cur, cur = 0, 0
        for v in nums:
            if v == 1:
                cur += 1
            else:
                cur = 0
            max_cur = cur if cur > max_cur else max_cur

        return max_cur