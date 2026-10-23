class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], prev = prev, arr[i] if arr[i] > prev else prev
        
        return arr