class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for l in range(len(arr)-1):
            res.append(max(arr[l+1:]))
        
        res.append(-1)

        return res
