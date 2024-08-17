class Solution:
    def productExceptSelf(self, nums):
        #code here
        output = [1] * len(nums)
        cur_prod = nums[0]
        for i in range(1, len(nums)):
            output[i] = cur_prod
            cur_prod *= nums[i]
        cur_prod = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= cur_prod
            cur_prod *= nums[i]
        return output
