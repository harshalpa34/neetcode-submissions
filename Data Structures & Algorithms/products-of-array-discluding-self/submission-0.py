class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Product of all numbers to the left
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # Product of all numbers to the right
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * right
            right = right * nums[i]

        return res