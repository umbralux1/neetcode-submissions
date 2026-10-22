class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev = -1

        for i in range(len(arr) -1, -1, -1):
            arr[i], prev = prev, max(prev, arr[i])
        
        return arr
