class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for rows in range(max(height)):
            i = j = 0

            while i < len(height) - 1:
                if rows >= height[i] or rows < height[i] and rows < height[i + 1]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    while j < len(height) and height[j] <= rows:
                        j += 1
                    if j != len(height):
                        water += j - i - 1
                    i = j       
        return water