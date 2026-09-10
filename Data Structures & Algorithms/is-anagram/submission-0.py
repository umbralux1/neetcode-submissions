class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.create_counter(s) == self.create_counter(t)
    

    def create_counter(self, x: str) -> dict[str]:
        counter = {k:0 for k in x}

        for c in x:
            counter[c] += 1
        
        return counter

