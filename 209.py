class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = max(nums)
        for i in range(len(nums)):
            if target == m:
                return 1
            elif target - m > 0:
                return self.minSubArrayLen(target = target - m,nums = nums.remove(m))+1
            else:
                return 0
