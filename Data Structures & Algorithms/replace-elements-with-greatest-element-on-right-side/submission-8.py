class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        res[len(arr)-1] = -1
        cur_max = arr[len(arr)-1]

        for i in range(len(arr)-1, 0, -1):
            # cur_max = max(arr[i], cur_max)
            cur_max = cur_max if cur_max > arr[i] else arr[i]
            res[i-1] = cur_max
        

        return res