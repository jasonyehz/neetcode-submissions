class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            tempStr = "".join(sorted(i))
            if tempStr not in d:
                d[tempStr] = []
            d[tempStr].append(i)
        return list(d.values())