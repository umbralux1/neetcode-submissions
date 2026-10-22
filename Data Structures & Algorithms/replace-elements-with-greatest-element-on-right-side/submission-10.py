class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        res[-1] = -1
        cur_max = arr[-1]

        for i in range(-1, -len(arr), -1):
            # cur_max = max(arr[i], cur_max)
            if arr[i] > cur_max:
                 cur_max = arr[i]
            res[i-1] = cur_max
        

        return res