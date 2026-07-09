class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = []
        numSet = set(nums)

        for i in nums:
            temp = []

            if i - 1 not in numSet:
                temp.append(i)

                while i + 1 in numSet:
                    temp.append(i + 1)
                    i += 1
            
            if len(temp) > len(result):
                result = temp
        
        return len(result)