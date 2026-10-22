class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = arr[-1]
        arr[-1] = -1
        original = arr[-1]
        
        for i in range(-1, -len(arr), -1):
            if original > cur_max:
                 cur_max = original
            original = arr[i-1]
            arr[i-1] = cur_max
        

        return arr