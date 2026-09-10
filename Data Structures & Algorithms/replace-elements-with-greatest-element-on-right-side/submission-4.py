class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxes = []
        max_cur = -1
        for i in range(len(arr)-1, -1, -1):
            maxes.append(max_cur)
            if max_cur < arr[i]:
                max_cur = arr[i]
        
        maxes.reverse()

        return maxes