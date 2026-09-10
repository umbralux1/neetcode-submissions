class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            res[anagram_hash(s)].append(s)
        
        return res.values()


def anagram_hash(s: str) -> int:
    res = [0] * 26
    
    for c in s:
        res[ord(c) - ord('a')] += 1
    
    return tuple(res)
