class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        # From 0 to 3
        for rows in range(max(height)):
            i = j = 0

            while i < len(height) - 1:
                #print(i,j)
                # When the space is empty at i or when the space and the next are occupied
                # Fix when i runs to end
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