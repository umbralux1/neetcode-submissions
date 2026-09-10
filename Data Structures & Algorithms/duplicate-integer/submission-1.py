class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)

        for v in c.values():
            if v > 1:
                return True
        
        return False