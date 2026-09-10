class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_cur = -1

        for i in range(len(arr)-1, -1, -1):
            max_cur, arr[i] = max(arr[i], max_cur), max_cur
        
        return arr