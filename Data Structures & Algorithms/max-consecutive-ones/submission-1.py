class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cur, cur = 0, 0
        for v in nums:
            if v == 1:
                cur += 1
            else:
                max_cur = max(cur, max_cur)
                cur = 0

        return max(cur, max_cur)