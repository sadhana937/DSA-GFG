class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        count = 1
        max_num = height[0]
        for i in range(1, len(height)):
            if height[i] > max_num:
                max_num = height[i]
                count += 1
        return count
