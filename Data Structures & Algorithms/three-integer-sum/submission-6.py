class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = sorted(nums)
        results = []

        for i in range(len(n) - 2):
            j, k = i + 1, len(n) - 1

            while j < k:
                if n[i] + n[j] + n[k] == 0:
                    temp = [n[i], n[j], n[k]]
                    if temp not in results:
                        results.append(temp)
                    j += 1

                if n[i] + n[j] + n[k] < 0:
                    j += 1
                
                if n[i] + n[j] + n[k] > 0:
                    k += -1

        return results