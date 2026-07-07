class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        freqList = sorted(d.items(), key = lambda x: x[1], reverse = True)

        result = []
        n = 0
        for i in range(k):
            tempPair = freqList[n]
            result.append(tempPair[0])
            n += 1

        return result