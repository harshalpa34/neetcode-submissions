class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right=1
        while left < len(nums):
            if (nums[left] + nums[right] == target):
            
                return [left, right]
            right = right + 1;
            if(right >= len(nums)):
                right=left+2
                left=left+1
        return [left, right] 