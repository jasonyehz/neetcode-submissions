class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for i in s:
            d[i] = d.get(i, 0) + 1
        for j in t:
            d[j] = d.get(j, 0) - 1
            if d.get(j, 0) == 0:
                d.pop(j)
        if d == {}:
            return True
        else: return False        
                