class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        count = 0
        h = nums[0]
        for i in range(1, len(nums)):
            h = max(nums[i], h)
            if nums[i] < nums[i - 1]:
                count += 1
                nums[i - 1]
            if count > 1:
                return False